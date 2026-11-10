---
title: Vue d’ensemble : Dérivée, gradient et règle de dérivation en chaîne
kurz: Vue d’ensemble
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15230100
summary: Comment un nombre réagit à ses entrées : de la tangente au mode inverse
tags: 
lang: fr
---

## De quoi il s’agit

Un nombre dépend souvent de beaucoup d’autres nombres. Le prix que la somme pondérée du [chapitre 1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) prédit pour un appartement dépend de chaque poids et de chaque caractéristique. La longueur d’un vecteur d’erreur dépend de chacune de ses composantes. Le résultat d’un long calcul dépend de chacune des valeurs par lesquelles il commence. Ce chapitre pose la question suivante : de combien et dans quel sens un tel nombre change-t-il lorsqu’on modifie un peu l’une de ses entrées ? Et lorsqu’il y a des milliers d’entrées : dans quelle direction faut-il les déplacer toutes à la fois pour que le nombre augmente ou diminue le plus vite possible ?

S’y ajoute une question pratique. Souvent, le nombre est le résultat d’une longue chaîne d’opérations simples. On pourrait modifier un peu chaque entrée séparément et regarder ce qui en résulte à la fin. Avec un million d’entrées, cela reviendrait à répéter tout le calcul un million de fois. Peut-on aller plus vite ? Et comment vérifier qu’une formule pour ces sensibilités, que l’on a soi-même établie ou programmée, est vraiment juste ?

À quoi cela sert : avec les réponses, on sait de quels boutons de réglage un résultat dépend le plus et comment de petites erreurs de mesure sur les entrées se répercutent sur le résultat. On peut remplacer une fonction compliquée, au voisinage d’un point, par une fonction beaucoup plus simple et estimer l’erreur ainsi commise. Et l’on peut calculer les sensibilités même lorsque le nombre est issu d’un très long calcul comportant un très grand nombre d’entrées. Presque toute méthode qui apprend à partir de données a besoin de ces outils.

**Comment travailler avec ce chapitre.** Les sections s’appuient les unes sur les autres, et chaque nouvelle notion a sa propre sous-section avec un exemple. Les encadrés dépliables contiennent le contexte (pourquoi une méthode fonctionne et d’où elle vient), les démonstrations et les preuves ; ils ne sont pas nécessaires pour poursuivre la lecture. Essayez d’abord de résoudre les exercices (de ★ à ★★★) vous-même et exécutez réellement les programmes ; la solution se déplie juste en dessous de chaque exercice.
