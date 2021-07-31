from session_12 import RegularPoly
from session_12_2 import RegularPolySeq
import os
import inspect
import re
import math
import pytest



def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001
    
    try:
        p = RegularPoly(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass
                       

    n = 4
    R = 1
    p = RegularPoly(n, R)
    assert p.interior_angle == 114.59155902616465, (f'actual: {p.interior_angle}, '
                                    ' expected: 114.59155902616465')
    assert math.isclose(p.area, 2, 
                        rel_tol=abs_tol, 
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')
    
    assert math.isclose(p.edge_length, math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.edge_length},'
                                          f' expected: {math.sqrt(2)}')
    
    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          f' expected: {4 * math.sqrt(2)}')
    
    assert math.isclose(p.apothem, 0.707,
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          ' expected: 0.707')
    p = RegularPoly(6, 2)
    assert math.isclose(p.edge_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    # assert math.isclose(p.interior_angle, 230,
    #                     rel_tol=rel_tol, abs_tol=abs_tol)
    
    p = RegularPoly(12, 3)
    assert math.isclose(p.edge_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    # assert math.isclose(p.interior_angle, 150,
    #                     rel_tol=rel_tol, abs_tol=abs_tol)
    
    p1 = RegularPoly(3, 10)
    p2 = RegularPoly(10, 10)
    p3 = RegularPoly(15, 10)
    p4 = RegularPoly(15, 100)
    p5 = RegularPoly(15, 100)
    
    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

def test_seq_iterable():
    polseq = RegularPolySeq(3, 3)
    try:
        iter(polseq)
    except:
        assert False, 'Your Polygon Sequence for this week must be an iterable'


def test_seq_iterator():
    polseq = RegularPolySeq(3, 3)
    try:
        next(iter(polseq))
    except:
        assert False, 'Your Polygon Sequence for this week must be an iterator'

