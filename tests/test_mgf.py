"""Testing for MGF class"""

# Import packages
from dataclasses import dataclass
import pytest
import numpy as np
from pathlib import Path
import warnings

# Skip all these tests if sage isn't installed in the environment
sage = pytest.importorskip('sage', reason="Sage is not installed")
from sage.all import *  # noqa: E402

warnings.filterwarnings("ignore")

# Set wd
project_root = Path(__file__).parents[1]
sagedir = project_root/'sage'
load_attach_path(str(sagedir))
sage.repl.load.load('mgf.sage', globals())


# Define dataclass for testing
@dataclass(frozen=True)
class TestEV:
    order: list
    tail_sol: Tail
    head_sol: list


# Test EV methods for obtaining Head and Tail of Eq 52 (printing)
# 10th order, 8th order, 5th order, 4th order, 3rd order (as raw, 2 + 1, 1 + 1 + 1),
#   2nd order (raw), 1st order, 0th order
ev_test_inputs = [
    TestEV(order=[1, 2, 3, 4],
           tail_sol=Tail(k=3, ev=[1, 2, 3, 3]),
           head_sol=list(np.repeat([Head(kj=(3, 3), ev=[1, 2, 3, 2]),
                                    Head(kj=(3, 2), ev=[1, 2, 2, 3]),
                                    Head(kj=(3, 1), ev=[1, 1, 3, 3]),
                                    Head(kj=(3, 0), ev=[0, 2, 3, 3])],
                                   [3, 3, 2, 1]))),
    TestEV(order=[4, 0, 2, 2],
           tail_sol=Tail(k=3, ev=[4, 0, 2, 1]),
           head_sol=list(np.repeat([Head(kj=(3, 3), ev=[4, 0, 2, 0]),
                                    Head(kj=(3, 2), ev=[4, 0, 1, 1]),
                                    Head(kj=(3, 0), ev=[3, 0, 2, 1])],
                                   [1, 2, 4]))),
    TestEV(order=[3, 2, 0, 1],
           tail_sol=Tail(k=3, ev=[3, 2, 0, 0]),
           head_sol=list(np.repeat([Head(kj=(3, 1), ev=[3, 1, 0, 0]),
                                    Head(kj=(3, 0), ev=[2, 2, 0, 0])],
                                   [2, 3]))),
    TestEV(order=[0, 4, 0, 0],
           tail_sol=Tail(k=1, ev=[0, 3, 0, 0]),
           head_sol=list(np.repeat(Head(kj=(1, 1), ev=[0, 2, 0, 0]),
                                   3))),
    TestEV(order=[0, 3, 0, 0],
           tail_sol=Tail(k=1, ev=[0, 2, 0, 0]),
           head_sol=list(np.repeat(Head(kj=(1, 1), ev=[0, 1, 0, 0]),
                                   2))),
    TestEV(order=[0, 2, 0, 1],
           tail_sol=Tail(k=3, ev=[0, 2, 0, 0]),
           head_sol=list(np.repeat(Head(kj=(3, 1), ev=[0, 1, 0, 0]),
                                   2))),
    TestEV(order=[1, 1, 1, 0],
           tail_sol=Tail(k=2, ev=[1, 1, 0, 0]),
           head_sol=[Head(kj=(2, 1), ev=[1, 0, 0, 0]), Head(kj=(2, 0), ev=[0, 1, 0, 0])]),
    TestEV(order=[0, 2, 0, 0],
           tail_sol=Tail(k=1, ev=[0, 1, 0, 0]),
           head_sol=[Head(kj=(1, 1), ev=[0, 0, 0, 0])])
]


@pytest.mark.parametrize("inputs", ev_test_inputs)
def test_ev(inputs, very_verbose):
    # Print unwrapping
    print(f'\nProcess {inputs.order} unwrapped as {EV.unwrap(inputs.order)}')

    # Print Tail
    m2s, m1 = recurse(inputs.order)
    if very_verbose:
        print(f'Tail:\n    k = {m1.k}, EV = {m1.ev} unwrapped as {EV.unwrap(m1.ev)}')
    assert m1 == inputs.tail_sol

    # Recursively unwrap head and tail
    if very_verbose:
        print('Heads:')
    for m2 in m2s:
        if very_verbose:
            print(f'    {m2.kj}, {m2.ev} unwrapped as {EV.unwrap(m2.ev)}')
    assert m2s == inputs.head_sol

    if very_verbose:
        print('-----')
