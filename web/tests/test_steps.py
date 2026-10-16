import sys, numpy as np
sys.path.insert(0, ".")
from engine.scene_model import ModelScene, _group_by_step

# grouping: default (no step) -> each its own; explicit step -> merged, ordered
specs = [{"step": 2}, {"step": 1}, {"step": 1}]
g = _group_by_step(specs)
assert [len(x) for x in g] == [2, 1], g          # step1 has 2, step2 has 1; ordered 1 then 2
print("group_by_step OK:", [len(x) for x in g])

def two_line_model(step0, step1):
    return {
        "objects": [
            {"id":"a","type":"Line","args":{"start":[-1,0,0],"end":[1,0,0]}},
            {"id":"b","type":"Line","args":{"start":[-1,1,0],"end":[1,1,0]}},
        ],
        "animations": [
            {"type":"Create","target":"a","run_time":1.0,"step":step0},
            {"type":"Create","target":"b","run_time":2.0,"step":step1},
        ],
        "background":[1,1,1],
    }

# Sequential: different steps -> total = 1 + 2 = 3
seq = ModelScene(two_line_model(0, 1)).build_timeline()
assert abs(seq.duration - 3.0) < 1e-9, seq.duration
print("sequential duration OK:", seq.duration)

# Parallel: same step -> total = max(1,2) = 2, both progress together
par = ModelScene(two_line_model(0, 0)).build_timeline()
assert abs(par.duration - 2.0) < 1e-9, par.duration
# at t=1: anim a (run_time 1) fully drawn; anim b (run_time 2) half drawn
par.seek(1.0)
a = par.objects_by_id["a"]; b = par.objects_by_id["b"]
# 'a' is a straight Create -> full length means its last point reached the end anchor [1,0,0]
assert np.allclose(a.points[-1], [1,0,0], atol=1e-9), a.points[-1]
# 'b' half-drawn: its last point should be near the middle x (between -1 and 1 => ~0), not the end
assert b.points[-1][0] < 0.6, b.points[-1]
print("parallel duration OK:", par.duration, "| a end:", a.points[-1][0], "| b front:", round(float(b.points[-1][0]),3))

print("\nSTEP TESTS PASSED")
