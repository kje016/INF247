# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
from sage.all import *
import HF_polynomial

#s22 = "0011011101010001101110"
s22 = "11001"
var('x')
R = PolynomialRing(GF(2), x)


def S(str_x):
    s_list = [int(x) for x in str_x]
    pol = sum([c*x**(e+1) for e,c in enumerate(s_list)])
    pol = pol + 1*x**0
    return pol


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

def is_done(a):
    return a == (0*x**0)


#a0 = x**(len(s22)+1)
a0 = S(s22)
a1 = x**2

U = [1*x**0, 0*x**0]
V = [0*x**0, 1*x**0]
A = [a0, a1]
Q = [0, HF_polynomial.pol_divide(a0,a1)]


def run_EEA(u, v, a, q):
    while not is_done(a[-1]):
        next_u = calc_u(q[-1], u[-1], u[-2])
        next_v = calc_v(q[-1], v[-1],v[-2] )
        next_a = calc_a(a[-2],q[-1],a[-1])

        a.append(next_a)
        u.append(next_u)
        v.append(next_v)
        if is_done(next_a):
            q.append(0)
            break
        next_q = HF_polynomial.pol_divide(a[-2], next_a)
        q.append(next_q)

    res = zip(u, v, a, q)
    for row in res:
        print(row)

    return u, v, a, q


EEA = run_EEA(U, V, A, Q)
print(EEA)