from .AnimObject import AnimObject
from .camera import Camera

# Web variant of Scene: instead of writing frames to ffmpeg, play()/wait() record a TIMELINE.
# The browser player then seek()s to any time t and paints the result to the Canvas. This makes
# playback real-time and scrubbable, without any encoder.


class Scene:
    def __init__(self):
        self.objectList: list[AnimObject] = []   # drawn in order
        self.timeline = []                       # list of {"anims": [...], "dur": seconds}
        self.camera = Camera()

    def add(self, *objects):
        self.objectList.extend(objects)
        return self

    def construct(self):
        """Override in a subclass: self.add(...) for static objects, self.play()/self.wait() for timing."""
        pass

    def play(self, *animations, run_time=None):
        """Play the given animations TOGETHER as ONE timeline segment (they run simultaneously).
        Pass run_time to force a common duration; otherwise each animation keeps its own run_time
        and the segment lasts as long as the slowest one. Separate play() calls run one after
        another - that is how sequence vs. parallelism is expressed."""
        for anim in animations:
            if run_time is not None:
                anim.run_time = run_time
            if anim.target not in self.objectList:
                self.objectList.append(anim.target)   # auto-add targets (e.g. Create of a new graph)
            anim.begin()                              # snapshot start state (current = end of previous)
        dur = max((anim.run_time for anim in animations), default=0.0)
        self.timeline.append({"anims": list(animations), "dur": dur})
        for anim in animations:
            anim.update(1.0)                          # advance to end so the NEXT begin() is correct

    def wait(self, duration=1.0):
        self.timeline.append({"anims": [], "dur": duration})

    # ---------- for the browser player ----------
    def build_timeline(self):
        """Run construct() to fill objectList + timeline. Call once before playback."""
        self.objectList = []
        self.timeline = []
        self.construct()
        return self

    @property
    def duration(self):
        return sum(seg["dur"] for seg in self.timeline) or 1e-6

    def seek(self, t):
        """Set every object's state to the scene at global time t (seconds)."""
        # segment time bounds
        bounds, cursor = [], 0.0
        for seg in self.timeline:
            bounds.append((cursor, cursor + seg["dur"]))
            cursor += seg["dur"]
        # Pass 1: every FUTURE animation -> its START state (update(0)). We go latest-first so that,
        # for an object touched by several segments, the EARLIEST future segment's reset wins. This
        # restores objects whose only/earliest animation is still ahead (e.g. a FadeOut's target must
        # be VISIBLE before it fades, a Shift's target at its pre-shift position).
        for (t0, _t1), seg in reversed(list(zip(bounds, self.timeline))):
            if t < t0:
                for anim in seg["anims"]:
                    anim.update(0.0)
        # Pass 2: past + current segments in order (these override the resets with the real state).
        for (t0, _t1), seg in zip(bounds, self.timeline):
            if t < t0:
                continue
            for anim in seg["anims"]:
                rt = anim.run_time if anim.run_time > 0 else seg["dur"]   # this anim's own duration
                if rt <= 0 or t >= t0 + rt:
                    anim.update(1.0)                                   # finished
                else:
                    anim.update((t - t0) / rt)                         # in progress, on its own clock
        self.run_updaters()        # after the frame's state is set, let objects recompute from it
        return self

    def run_updaters(self):
        """Run every object's updaters (and its children's) for the current frame."""
        for obj in self.objectList:
            obj.run_updaters()
        return self
