# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
from sage.all import *
import HF_polynomial

"""Extended Euclidean Algorithm is faster"""

"""Example taken from lecture notes p.73"""
var('x')
R = PolynomialRing(GF(2), x)
sN = "0011011101010001101110"
N = len(sN)

def S(str_x):
    s_list = [int(x) for x in str_x]
    pol = sum([c*x**(e+1) for e,c in enumerate(s_list)])
    pol = pol + 1*x**0
    return pol


def is_done(preva, crnta, n):
    if preva.degree(x) > ((n+1)/2) and crnta.degree(x) <= ((n+1)/2):
        return True
    return False


def calc_u(crnt_q, crnt_u, prev_u):
    next_u = HF_polynomial.pol_mult(crnt_q,crnt_u)
    next_u = HF_polynomial.pol_add(next_u, prev_u)
    return next_u


def calc_v(crnt_q, crnt_v, prev_v):
    next_v = HF_polynomial.pol_mult(crnt_q, crnt_v)
    next_v = HF_polynomial.pol_add(next_v, prev_v)
    return next_v


def calc_a(prev_a, crnt_q, crnt_a):
    next_a = HF_polynomial.pol_mult(crnt_q, crnt_a)
    next_a = HF_polynomial.pol_add(prev_a, next_a)
    return next_a



a0 = x**(N+1)
a1 = S(sN)

U = [1*x**0, 0*x**0]
V = [0*x**0, 1*x**0]
A = [a0, a1]
Q = [0, HF_polynomial.pol_divide(a0, a1)]


def run_BKM(u, v, a, q):
    while not is_done(a[-2], a[-1], N):
        next_u = calc_u(q[-1], u[-1], u[-2])
        next_v = calc_v(q[-1], v[-1], v[-2])
        next_a = calc_a(a[-2], q[-1], a[-1])

        a.append(next_a)
        u.append(next_u)
        v.append(next_v)

        next_q = HF_polynomial.pol_divide(a[-2], next_a)
        q.append(next_q)
    print("-----------------------------------------------------------------------------------------")
    res = zip(u, v, a, q)
    for row in res:
        print(row)
    print("-----------------------------------------------------------------------------------------")
    return u, v, a, q

U, V, A, Q = run_BKM(U, V, A, Q)


def comp_fx(L, cx):
    result = []
    for a,b in cx.coefficients():
        result.append([a,L-b])
    return sum([c*x**e for c,e in result])


Cx = V[-1]
dx = HF_polynomial.pol_mult(a1, Cx)
dx = HF_polynomial.pol_gcd(dx, a0)
L = max(Cx.degree(x), dx.degree(x))
arg2_fx = HF_polynomial.pol_divide(Cx, x)
fx = comp_fx(L, Cx)

print(f"S(X)= {a1}")
print(f"C(X)= {Cx} from EEA")
print(f"D(X)= {dx} from X^(N+1)")
print(f"L=max(deg(C(X), deg(D(X))= max({Cx.degree(x)}, {dx.degree(x)}) = {L}")
print(f"the generating polynomial is= {fx}")



