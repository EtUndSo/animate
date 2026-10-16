"""Function interaction: combine functions into new functions (the computation layer for 1D).

These return plain callables f(x) so they plot through the normal pipeline (plot_graph) and can be
driven by a ValueTracker via updaters like any other function.
"""
import numpy as np


def make_convolution(f, g, a, b, n=240):
    """Numerical convolution (f * g)(t) = ∫ f(τ) g(t−τ) dτ over τ in [a, b] (trapezoid rule).
    f and g must accept a numpy array (our parsed functions do, being numpy expressions)."""
    taus = np.linspace(a, b, n)
    w = np.full(n, (b - a) / (n - 1))
    w[0] *= 0.5
    w[-1] *= 0.5                                   # trapezoid weights
    ftau = f(taus) * np.ones(n)                    # broadcast constants to an array

    def h(t):
        return float(np.sum(w * ftau * g(t - taus)))

    return h


def make_product(f, g):
    return lambda x: f(x) * g(x)


def make_sum(f, g):
    return lambda x: f(x) + g(x)


def make_difference(f, g):
    return lambda x: f(x) - g(x)
