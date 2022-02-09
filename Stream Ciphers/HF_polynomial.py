from sage.all import *

R = GF(2)['x']
var('x')


def list_to_pol(input_list):
    return sum([c*x**e for c,e in input_list])


def pol_add(a0, a1):
    a0 = a0.coefficients()
    a1 = a1.coefficients()

    result = []
    for index, elem in enumerate(a0):
        if not(elem in a1):
            result.append(elem)
    for index,elem in enumerate(a1):
        if not(elem in a0):
            result.append(elem)

    result = list_to_pol(result)
    return result


def pol_mult(pol1, pol2):
    if pol1 == 0*x**0 or pol2 == 0*x**0:
        return 0*x**0
    exp_pol1 = [b for a,b in pol1.coefficients()]
    exp_pol2 = [b for a,b in pol2.coefficients()]

    # product of polynomials = sum of exponents
    result = [a+b for a in exp_pol1 for b in exp_pol2]

    result_mod2 = {}
    for index, elem in enumerate(result):
        result_mod2.update({elem: (result_mod2.get(elem, 0)+1) % 2})

    pol_prod = sum([c*x**e for e,c in result_mod2.items()])
    return pol_prod


def pol_divide(dividend, divisor):
    #a0_exp = [b for a, b in dividend.coefficients()]
    #a1_exp = [b for a, b in divisor.coefficients()]
    #count = 0

    crnt_dd = dividend
    crnt_dr = divisor
    result = []
    while crnt_dr.degree(x) <= crnt_dd.degree(x):
        prod = crnt_dd.degree(x) - crnt_dr.degree(x)
        divide_by = pol_mult(crnt_dr, x**prod)
        crnt_dd = pol_add(crnt_dd, divide_by)
        result.append(prod)
        if crnt_dd == 0:
            break
    return sum([x**e for e in result])


def pol_gcd(dividend, divisor):
    crnt_dd = dividend
    crnt_dr = divisor
    result = []
    while crnt_dr.degree(x) <= crnt_dd.degree(x):
        prod = crnt_dd.degree(x) - crnt_dr.degree(x)
        divide_by = pol_mult(crnt_dr, x**prod)

        crnt_dd = pol_add(crnt_dd, divide_by)
        result.append(prod)
        if crnt_dd == 0:
            break
    if crnt_dd == 1:
        return x**0
    return crnt_dd