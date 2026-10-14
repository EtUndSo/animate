# Rate (easing) functions: map raw progress t in [0,1] to eased progress in [0,1].

def linear(t):
    return t

def smooth(t):
    """Smoothstep: eases in and out (zero slope at 0 and 1) - looks far more natural than linear."""
    return t * t * (3 - 2 * t)
