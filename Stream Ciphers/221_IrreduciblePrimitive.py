# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
""" Example form Lecture notes p.49 """
from sage.all import *
import HF_polynomial as HF

var('x')
R = PolynomialRing(GF(2), 'x')
R.inject_variables()


def create_possible_states(list_len):
    output_list = []
    x_n = []
    for i in range((2**list_len)):
        bit = "{0:b}".format(i)
        padding = "0" * (list_len - len(bit))
        bit_string = padding + bit
        x_n.append([int(a) for a in bit_string])
        output_list.append(bit_string)
    return output_list, x_n


def deriv_modn(pol, modn):
    der = derivative(pol)
    der = der.coefficients(x)
    der = [[int(a)%modn,b] for a, b in der]
    result = []
    for elem in der:
        if elem[0] == 0:
            continue
        else:
            result.append(elem)
    result = sum([c*x**e for c,e in result])
    return result


def pol_gcd(dividend, divisor):
    crnt_dd = dividend
    crnt_dr = divisor
    result = []
    while crnt_dr.degree() <= crnt_dd.degree():
        prod = crnt_dd.degree() - crnt_dr.degree()
        divide_by = crnt_dr * (x**prod)

        crnt_dd = crnt_dd + divide_by
        result.append(prod)
        if crnt_dd == 0:
            break
    if crnt_dd == 1:
        return x**0
    return crnt_dd


def create_B_E(pol):
    B, n = [], pol.degree()
    for i in range(n):
        gi = x**(2*i)
        gi = pol_gcd(gi, pol)
        B.append(gi)

    for i_row, row in enumerate(B):
        res = [0]*(len(B))
        for j in row.exponents():
            res[j] = 1
        B[i_row] = res
    B = matrix(GF(2), B)
    E = identity_matrix(GF(2), B.nrows())
    return B + E

fx = x**6 + x**5 + x**4 + x**3 + x**2 + x + x**0
der_fx = derivative(fx)
w_mul_roots = gcd(fx, der_fx)   # if wo_mul_roots f=f1f2 is a product of its coprime factors (p48)
B_E = create_B_E(fx)

num_solution = 2**(B_E.nrows()-B_E.rank())
print(f"number of solutions:= {num_solution}")
"""There are 2 trivial solutions, so if num_solutions == 2
    the polynomial is irreducible"""

if num_solution != 2:
    solutions = []
    solution_mat = B_E
    _, x_vars = create_possible_states(solution_mat.ncols())
    for pol in x_vars:
        if vector(pol)*solution_mat == 0:
            solutions.append(pol)
    for i, elem in enumerate(solutions):
        solutions[i] = sum([b*x**a for a,b in enumerate(elem)])
    print(f"non-trivial solutions := {solutions}")
    #TODO: choose one solution, name it g. take gcd(f,g). factorize g, and that is the solution

else:
    print(f"fx=({fx}) is irreducible")


