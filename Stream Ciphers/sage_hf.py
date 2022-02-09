# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'

from sage.all import *
from sage.crypto.boolean_function import BooleanFunction

var('x')
R = PolynomialRing(GF(2), x)
R.inject_variables()
x_vars = 3

fx = x**4 + x + 1

b_vars = 4
B = BooleanPolynomialRing(b_vars, x)
B.inject_variables()


def create_possible_states(list_len):
    output_list = []
    x_n = []
    for i in range((2**list_len)):
        bit = "{0:b}".format(i)
        padding = "0" * (list_len - len(bit))
        bit_string = padding + bit
        x_n.append([int(x) for x in bit_string])
        output_list.append(bit_string)
    return output_list, x_n


# Given a feedbackfunction, check the period
def check_period(input_pol):
    all_states = []
    crnt_state = [0]*x_vars
    while crnt_state not in all_states:
        all_states.append(crnt_state)
        input_bit = input_pol.substitute(x0=crnt_state[0], x1=crnt_state[1], x2=crnt_state[2])
        crnt_state = [input_bit]+crnt_state[:x_vars-1]
    period = len(all_states)
    return period, (2**x_vars == period)


# Important to check if amountof variables is correct
def truthcol_to_var(lexi_vars):
    pol = []
    for i in range(len(lexi_vars)):
        pol.append(B(str(x)+str(i))*lexi_vars[i])
    #pol = [x1*lexi_string[0], x2*lexi_string[1], x3*lexi_string[2], x4*lexi_string[3]]
    output = 1*x0**0        #x0 if in BooleanPolRing, x if in PolRing
    for elem in pol:
        if elem != 0:
            output = output*elem
    return output


def C_to_f(c):
    n_vars = log(len(c), 2)
    _, lexi_variables = create_possible_states(n_vars)
    f = 0*x0**0
    for i, elem in enumerate(c):
        if elem == 1:
            f = f+(truthcol_to_var(lexi_variables[i]))
    print(f)
    return f

#Cf = C_to_f((0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0))
#print(f"Cf := {Cf}")

#input_pol should be in PolynomialRing
# creating the matrix as in p.100 in lecture notes
def companion_matrix(input_pol):
    pol_col = input_pol.list()[::-1]
    pol_col.pop(0)
    id_matrix = [list(i) for i in (identity_matrix(GF(2), input_pol.degree()-1))]
    id_matrix.append([0]*(input_pol.degree() -1))
    [id_matrix[i].insert(0, pol_col[i]) for i in range(len(id_matrix))]
    return Matrix(id_matrix)



A = companion_matrix(fx)
breakpoint()
print(A)

