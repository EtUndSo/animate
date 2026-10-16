import sys, numpy as np
sys.path.insert(0, ".")
from engine.axes import Axes
from engine.plotting import plot_graph
from engine import scene_model as SM

ax = Axes(x_range=(-6, 6), y_range=(-2, 2), x_length=12, y_length=5)
def segs(fn, x0=None, x1=None):
    return plot_graph(fn, ax.x_min if x0 is None else x0, ax.x_max if x1 is None else x1,
                      ax.coords_to_point, ax.x_length)

def npts(ss): return sum(len(s) for s in ss)

# straight line -> ONE piece; far fewer points than a dense oscillation (adaptive)
s = segs(lambda x: x)
assert len(s) == 1, len(s)
line_pts = npts(s)
print("line OK: 1 piece,", line_pts, "pts")

# sin(x) -> one smooth piece, open (first != last), reasonably dense
s = segs(np.sin)
assert len(s) == 1
assert not np.allclose(s[0][0], s[0][-1]), "graph must be OPEN (Create L->R)"
# smoothness: every bend angle between anchors is small (<~12 deg) -> no spikes
pts = s[0][::3]                      # anchors
def bend(a,b,c):
    v1=b-a; v2=c-b; n1=np.linalg.norm(v1); n2=np.linalg.norm(v2)
    if n1<1e-9 or n2<1e-9: return 0
    return np.degrees(np.arccos(np.clip(np.dot(v1,v2)/(n1*n2),-1,1)))
maxbend = max(bend(pts[i-1],pts[i],pts[i+1]) for i in range(1,len(pts)-1))
assert maxbend < 15, ("sin not smooth, max bend", maxbend)
print("sin(x) OK: 1 open piece, max bend %.1f deg" % maxbend)

# high frequency sin(1000x): still ONE piece but DENSE (not a sparse fake wave)
s = segs(lambda x: np.sin(1000*x))
assert len(s) == 1
assert npts(s) > max(2000, line_pts*3), ("sin(1000x) must be far denser than a line", npts(s))
print("sin(1000x) OK: dense", npts(s), "pts vs line", line_pts, "(honest, not a fake slow wave)")

# tan(x): poles -> SPLIT into multiple pieces, never a line across the asymptote
s = segs(np.tan)
assert len(s) >= 3, ("tan should split at poles", len(s))
print("tan(x) OK: split into", len(s), "pieces at the poles")

# discontinuity values are not drawn (no huge jumps within a piece)
for seg in s:
    ys = seg[:,1]
    assert np.all(np.abs(ys) < 1e4), "a pole value leaked into a piece"
print("no pole lines OK")
print("\nPLOTTING TESTS PASSED")
