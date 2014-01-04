import c2_solve_formula
import time

examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
GLITTERS is not GOLD
ONE < TWO < THREE
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def test():
    t0 = time.clock()
    for example in examples:
        print; print 13*' ', example
        print '%6.4f sec:    %s  ' % timedcall(c2_solve_formula.solve, example)
    print '%6.4f tot.' % (time.clock()-t0)

#test()

import cProfile
cProfile.run('test()')
