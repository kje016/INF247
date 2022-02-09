# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
"""Reffering to Theorem 5 lecture notes p.56"""
from sage.all import *
s10 = "0010001111"

def discrepency(index, Sn):
    Sns = Sn

    d = list(s10[0:index])
    d = sum([int(x) for x in d])%2
    return d%2


def gen_pol_deg(deg):
    breakpoint()
    result = []
    var('x')
    R= PolynomialRing(GF(2),x)
    monics_it = R.monics(deg)
    for pol in monics_it:
        result.append(pol)
    return result

# returns next_LN, next_fN
def case1(index):
    next_SN = s10[0:index+1]
    next_SN = [int(x) for x in next_SN]
    if next_SN == [0]*(index+1):
        return 0,1
    if next_SN == ([0]*(index)+[1]):
        return index+1, gen_pol_deg(index+1)
    return False

def case2(index, Sn):
    discrepency(index, Sn)
case1(2)