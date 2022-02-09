# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
from sage.all import *
from sage.crypto.boolean_function import BooleanFunction

var('x')
x_vars = 3
R = BooleanPolynomialRing(x_vars, x)
R.inject_variables()

f = 1+x1 +x2 + x0*x1 + x1*x2

# Is singular if polynomials highest lex var has degree 1.
def is_singular(input_pol):
    terms = [a for a in input_pol.terms() if R(str(x)+str(x_vars-1)) in a]
    for term in terms:
        if term.degree() > 1:
            return False
        else: continue
    return True


def check_period(input_pol):
    all_states = []
    crnt_state = [0]*x_vars
    while crnt_state not in all_states:
        all_states.append(crnt_state)
        input_bit = input_pol.substitute(x0=crnt_state[0], x1=crnt_state[1], x2=crnt_state[2])
        crnt_state = [input_bit]+crnt_state[:x_vars-1]
    period = len(all_states)
    return period, (2**x_vars == period)

print(f"{f}: is singular = {is_singular(f)}")
period, is_deBruijn = check_period(f)
print(f"2^{x_vars} == {period}")
print(f"therfore is_deBruijn := {is_deBruijn}")


"""         General way of constructing deBruijn NFSR       """



