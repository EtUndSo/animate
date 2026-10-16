import sys, numpy as np
sys.path.insert(0, "."); sys.path.insert(0, "py")
from engine.scene_model import ModelScene
from engine.renderer import paint_scene
from engine.text import DecimalNumber

class Stub:
    def __init__(s): s.paths=[]; s.texts=[]
    def background(s,c): pass
    def draw_path(s,*a): s.paths.append(a)
    def draw_text(s, text, *a): s.texts.append(text)

def find(obj, cls, out):
    if isinstance(obj, cls): out.append(obj)
    for c in obj.subObjects: find(c, cls, out)

# Riemann with a DecimalNumber child (the computed area result)
model = {
  "objects": [
    {"id":"ax","type":"Axes","args":{"x_range":[0,3.2],"y_range":[-0.2,1.2],"x_length":12,"y_length":6}},
    {"id":"r","type":"Riemann","args":{"func":"sin(x)","count":12,"color":[0.35,0.6,0.92],"fill_opacity":0.5},
     "children":[{"id":"area","type":"DecimalNumber","result":{"key":"area"},"args":{"position":[2.5,1.0,0],"font_size":38,"color":[0,0,0],"decimals":3,"prefix":"A ≈ "}}]},
  ],
  "animations": [], "background":[1,1,1],
}
sc = ModelScene(model); sc.construct()

# expected midpoint area
n=12; x0,x1=0,3.2; dx=(x1-x0)/n
area = sum(np.sin(x0+(i+0.5)*dx) for i in range(n))*dx

nums=[]; find(sc.objects_by_id["r"], DecimalNumber, nums)
assert len(nums)==1, len(nums)
assert abs(nums[0].value - area) < 1e-9, (nums[0].value, area)
assert nums[0].text == f"A ≈ {area:.3f}", nums[0].text
print("Riemann result-child OK: value", round(nums[0].value,4), "text", repr(nums[0].text))

# it renders as text
p=Stub(); paint_scene(p, sc.objectList, sc.camera, background=[1,1,1])
assert any(t.startswith("A ≈") for t in p.texts), p.texts
print("area text drawn OK")

# hidden child -> not built / not drawn
model["objects"][1]["children"][0]["visible"]=False
sc2 = ModelScene(model); sc2.construct()
nums2=[]; find(sc2.objects_by_id["r"], DecimalNumber, nums2)
assert len(nums2)==0, "hidden child should not be built"
print("hidden child skipped OK")

print("\nCHILDREN TESTS PASSED")
