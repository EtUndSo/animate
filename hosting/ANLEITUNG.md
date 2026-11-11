# EtUndSo vom Raspberry Pi ausliefern

Stand 11.11.2026. Ziel: Die Website kommt dauerhaft vom eigenen Raspberry Pi 5 (8 GB, 4-TB-NVMe). Cloudflare bleibt davor für HTTPS, Schutz und Zwischenspeicher.

```
Besucher ──HTTPS──► Cloudflare (Zwischenspeicher, Zähler-Worker /api/count)
                        │  Cloudflare Tunnel (vom Pi aus aufgebaut, kein offener Port am Router)
                        ▼
                Raspberry Pi: Caddy (nur 127.0.0.1:8080) ─► /srv/etundso/repo/web
                        ▲
                        └── holt alle 2 Minuten den neuen Stand von GitHub (etundso-deploy.timer)
```

**Vorgehen:**
- Zuerst läuft alles unter der Testadresse `pi.etundso.de`. Erst wenn dort alles stimmt, wird `etundso.de` umgestellt (Schritt 10).
- Das Cloudflare-Pages-Projekt bleibt bis dahin unverändert und danach als Rückfall stehen.

Dateien in diesem Ordner: `Caddyfile`, `etundso-deploy` (Skript), `etundso-deploy.service`, `etundso-deploy.timer`, `worker-zaehler/worker.js`.

Befehle mit `sudo` laufen **auf dem Pi** (per SSH). Ein `…` steht für etwas, das du selbst einsetzt.

---

## 1. Betriebssystem

**A) Die NVMe ist leer (empfohlen):** Raspberry Pi OS **Lite (64-bit)** direkt auf die NVMe.
- Mit dem Raspberry Pi Imager auf einen USB-NVMe-Adapter schreiben, oder zuerst auf eine SD-Karte und von dort auf die NVMe kopieren.
- Einstellungen im Imager:
  - Hostname `etundso`;
  - eigener Benutzer;
  - SSH **nur mit öffentlichem Schlüssel**;
  - Zeitzone Europe/Berlin;
  - kein WLAN, ein LAN-Kabel ist stabiler.
- Startreihenfolge: `sudo raspi-config` → Advanced Options → Boot Order → NVMe/USB Boot.

**B) Auf der NVMe liegen schon Daten:** nichts überschreiben.
- Das System bleibt auf der SD-Karte, die Website liegt auf der NVMe.
- Ein Ordner auf der NVMe wird nach `/srv/etundso` eingebunden, damit alle Pfade dieser Anleitung gleich bleiben. Beispiel, die NVMe ist unter `/mnt/nvme` eingehängt:
  ```
  sudo mkdir -p /mnt/nvme/etundso /srv/etundso
  echo '/mnt/nvme/etundso /srv/etundso none bind,nofail 0 0' | sudo tee -a /etc/fstab
  sudo mount /srv/etundso
  ```

## 2. Grundsicherung
```
sudo apt update && sudo apt full-upgrade -y
sudo apt install -y unattended-upgrades ufw git curl
sudo dpkg-reconfigure -plow unattended-upgrades          # „Ja“: Sicherheitsupdates automatisch
sudo ufw allow from 192.168.0.0/16 to any port 22 proto tcp   # SSH nur aus dem Heimnetz (Netz ggf. anpassen)
sudo ufw enable
```
Passwort-Anmeldung per SSH abschalten. Das erst tun, wenn die Anmeldung mit Schlüssel sicher funktioniert:
```
echo 'PasswordAuthentication no' | sudo tee /etc/ssh/sshd_config.d/kein-passwort.conf
sudo systemctl restart ssh
```

## 3. Benutzer und Repo
Ein eigener Systembenutzer `etundso` holt das Repo. Er darf nur lesen (Deploy-Key).
```
sudo useradd --system --create-home --home-dir /srv/etundso --shell /usr/sbin/nologin etundso
sudo chmod 755 /srv/etundso
sudo -u etundso mkdir -m 700 -p /srv/etundso/.ssh
sudo -u etundso ssh-keygen -t ed25519 -N "" -C "etundso-pi" -f /srv/etundso/.ssh/id_ed25519
sudo cat /srv/etundso/.ssh/id_ed25519.pub
```
Den ausgegebenen Schlüssel auf GitHub eintragen: Repo **EtUndSo/animate** → Settings → Deploy keys → Add deploy key, **ohne** Schreibrecht. Dann:
```
sudo -u etundso ssh -o StrictHostKeyChecking=accept-new -T git@github.com   # Meldung „successfully authenticated“ ist richtig
sudo -u etundso git clone --depth 1 --branch main git@github.com:EtUndSo/animate.git /srv/etundso/repo
```
Geholt wird nur der aktuelle Stand ohne Geschichte (`--depth 1`), im November 2026 etwa 650 MB, davon `web/` etwa 430 MB.

## 4. Webserver Caddy
```
sudo apt install -y caddy
sudo cp /srv/etundso/repo/hosting/Caddyfile /etc/caddy/Caddyfile
sudo caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
sudo systemctl restart caddy
curl -sI http://127.0.0.1:8080/ | head -3                  # erwartet: HTTP/1.1 200 OK
curl -sI http://127.0.0.1:8080/wissen/ | head -1           # erwartet: 200
```
Caddy hört nur auf dem Pi selbst (127.0.0.1). Von außen ist er nur über den Tunnel erreichbar. Zugriffsprotokolle mit IP-Adressen schreibt Caddy in dieser Einstellung nicht.

## 5. Cloudflare-Zugang zum Leeren des Zwischenspeichers
Nach jedem neuen Stand leert der Pi den Zwischenspeicher von Cloudflare. Dafür braucht er einen eng begrenzten Schlüssel:
- **Schlüssel anlegen:** Cloudflare-Dashboard → Profil (oben rechts) → API Tokens → Create Token → Custom token.
  - Permissions: **Zone · Cache Purge · Purge**.
  - Zone Resources: **Include · Specific zone · etundso.de**.
  - Den Schlüssel kopieren.
- **Zone ID:** Dashboard → etundso.de → Overview, rechts unten „Zone ID“.
```
sudo mkdir -p /etc/etundso
sudo install -m 640 -o root -g etundso /dev/null /etc/etundso/cloudflare.env
sudo nano /etc/etundso/cloudflare.env
```
Inhalt, genau zwei Zeilen:
```
CF_ZONE_ID=…
CF_API_TOKEN=…
```

## 6. Automatisch aktualisieren
```
sudo install -m 755 /srv/etundso/repo/hosting/etundso-deploy /usr/local/bin/etundso-deploy
sudo cp /srv/etundso/repo/hosting/etundso-deploy.service /srv/etundso/repo/hosting/etundso-deploy.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now etundso-deploy.timer
systemctl list-timers etundso-deploy.timer                  # nächster Lauf in höchstens 2 Minuten
journalctl -u etundso-deploy -n 20                         # „Neuer Stand …“, „Cloudflare-Zwischenspeicher geleert“
```
Ab jetzt gilt: Nach deinem `git push` ist der neue Stand spätestens nach etwa 2 Minuten auf dem Pi.

## 7. Cloudflare Tunnel (zuerst mit der Testadresse)
- **Tunnel anlegen:** Cloudflare Zero Trust (one.dash.cloudflare.com) → Networks → Tunnels → Create a tunnel → **Cloudflared**.
  - Name: `etundso-pi`.
  - Umgebung: **Debian**, **arm64-bit**.
- **Auf dem Pi:** Die angezeigten Befehle laufen lassen. Sie installieren `cloudflared` und richten ihn mit `sudo cloudflared service install …` als Dienst ein. Im Dashboard muss der Tunnel danach „Healthy“ zeigen.
- **Public Hostname hinzufügen:** Subdomain `pi`, Domain `etundso.de`, Service **HTTP**, URL `localhost:8080`.
- **Test im Browser:** `https://pi.etundso.de` muss die Startseite zeigen.

Fragt Zero Trust beim ersten Öffnen nach einem Tarif, den kostenlosen Plan „Free“ wählen. Verlangt es Zahlungsdaten und das möchtest du nicht, gibt es einen Weg nur über die Kommandozeile (`cloudflared tunnel login`); sag dann Bescheid.

## 8. Besucherzähler als Cloudflare Worker
Der Zähler (`/api/count`) war eine Pages-Funktion. Er wird ein eigener kleiner Worker mit denselben Zahlen.
- **Worker anlegen:** Dashboard → Workers & Pages → Create → Worker.
  - Name `etundso-zaehler` → Deploy.
  - **Edit code:** den Inhalt von `hosting/worker-zaehler/worker.js` einfügen → Deploy.
- **Speicher binden:**
  - Worker → Settings → Bindings → Add → **KV namespace**.
  - Variable name: `COUNTERS`.
  - Namespace: **derselbe wie bisher beim Pages-Projekt**, zu sehen unter Pages-Projekt → Settings → Bindings.
- **Routen:** Worker → Settings → Domains & Routes → Add → **Route**:
  - `pi.etundso.de/api/*`, Zone etundso.de;
  - später zusätzlich `etundso.de/api/*`.
- **Test:** `https://pi.etundso.de/api/count?mode=read` zeigt die bisherigen Zahlen.

## 9. Zwischenspeicher-Regel
Damit fast alle Aufrufe aus dem Cloudflare-Zwischenspeicher kommen und der Pi kaum etwas hochladen muss:
- **Regel anlegen:** Dashboard → etundso.de → Caching → Cache Rules → Create rule, Name „EtUndSo vom Pi“.
  - **Custom filter expression** (Edit expression):
    ```
    (http.host in {"etundso.de" "pi.etundso.de"} and not starts_with(http.request.uri.path, "/api/"))
    ```
  - Cache eligibility: **Eligible for cache**.
  - Edge TTL: **Ignore cache-control header and use this TTL** → **1 month**.
  - Browser TTL: **Respect origin TTL**. Caddy schickt `no-cache`, Browser fragen also nach und bekommen meist ein schnelles 304.
- **Wirkung:** Ein neuer Stand wird trotzdem sofort sichtbar, weil `etundso-deploy` nach jedem Stand den Zwischenspeicher leert.

**Danach gib mir Bescheid.** Ich prüfe dann von meinem Rechner aus `pi.etundso.de`:
- Seiten, saubere Adressen ohne `.html`, 404;
- Abbildungen und Animationen, Suche, Editor;
- Zähler;
- Zwischenspeicher (`cf-cache-status: HIT`).

## 10. Umstellen auf etundso.de
Erst wenn Schritt 9 geprüft ist. Kurze Unterbrechung von wenigen Minuten möglich.
1. **Pages-Domain lösen:** Cloudflare-Dashboard → Workers & Pages → Pages-Projekt → **Custom domains** → `etundso.de` entfernen.
2. **Tunnel-Adresse hinzufügen:** Tunnel `etundso-pi` → Public Hostname → Add: Subdomain leer, Domain `etundso.de`, Service HTTP `localhost:8080`. Meldet das Dashboard einen vorhandenen DNS-Eintrag, diesen alten Eintrag für `etundso.de` unter DNS löschen und erneut hinzufügen.
3. **Zähler-Route:** Beim Worker die Route `etundso.de/api/*` ergänzen (Schritt 8).
4. **www:** `www.etundso.de` bleibt wie besprochen eine Weiterleitung auf `https://etundso.de` (DNS-Eintrag `www` AAAA `100::`, proxied, dazu eine Redirect Rule).
5. **Bescheid geben:** Ich prüfe `etundso.de` vollständig und passe die Datenschutzerklärung an (eigener Server, Cloudflare als Zwischenspeicher und Tunnel, keine Zugriffsprotokolle auf dem Pi).

**Rückfall:** Tunnel-Adresse `etundso.de` entfernen und die Custom Domain im Pages-Projekt wieder hinzufügen. Das Pages-Projekt bleibt dafür stehen. Wenn es später wegen der Dateigrenze nicht mehr baut, schadet das nicht, die Website kommt dann ja vom Pi.

## 11. Betrieb
- **Updates:** Sicherheitsupdates kommen automatisch (Schritt 2). Etwa einmal im Monat `sudo apt full-upgrade -y` und bei Bedarf neu starten.
- **Nach Stromausfall:** Caddy, cloudflared und der Timer starten von selbst wieder.
- **Kontrolle:**
  - `journalctl -u etundso-deploy -n 20` zeigt, ob der neueste Stand angekommen ist;
  - `systemctl status caddy cloudflared` zeigt, ob die Dienste laufen.
- **Ausfall-Meldung:** Cloudflare-Dashboard → Notifications → Add → **Tunnel Health Alert** (Mail, wenn der Tunnel ausfällt).
- **Sicherung:** nicht nötig für die Website, alles liegt im Git-Repo. Auf dem Pi sind nur `/etc/etundso/cloudflare.env` und der Deploy-Schlüssel eigen; beide lassen sich jederzeit neu anlegen.
- **Ändern am Pi:** Neue Fassungen von `Caddyfile`, Skript oder Timer kommen mit dem Repo. Übernommen werden sie erst, wenn Schritte 4 und 6 erneut ausgeführt werden; das passiert absichtlich nicht automatisch.
