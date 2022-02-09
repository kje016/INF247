# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
from sage.all import *
import copy
from sage.crypto.boolean_function import BooleanFunction

x_vars = 4
var('x')
B = BooleanPolynomialRing(x_vars, 'x')
B.inject_variables()
annihilator_degree = 2
# F ordered lexicographically
# from lecture notes p.107
def F(x_list):
    x1, x2, x3, x4 = x_list
    func = x4 + x3 + x2+ x2*x4 + x2*x3 + x2*x3*x4 + x1 + x1*x4 + x1*x2*x4
    return func%2


# ordered lexicographically rising
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


# Important to check if amount of variables is correct
def lexi_to_var(lexi_string):
    pol = [x0*lexi_string[0], x1*lexi_string[1], x2*lexi_string[2], x3*lexi_string[3]]
    output = 1*x0**0
    for elem in pol:
        if elem != 0:
            output = output*elem
    return output


def C_to_f(c):
    n_vars = log(len(c), 2)
    _, lexi_vars = create_possible_states(n_vars)
    f = 0*x0**0
    for i, elem in enumerate(c):
        if elem == 1:
            f = f+(lexi_to_var(lexi_vars[i]))
    return f


def annihilators_truth_table(truth_col):
    annihilators = [[0]]
    if truth_col[0] == 0:
        annihilators.append([1])

    for i in range(1, len(truth_col)):
        copies = copy.deepcopy(annihilators)
        annihilators = [ani+[0] for ani in annihilators]
        if truth_col[i] == 0:
            ones = [annihi+[1] for annihi in copies]
            annihilators.extend(ones)
    return annihilators


def valid_annihilators(truth_table, input_pol):
    output = []
    for i, elem in enumerate(truth_table):
        comp = C_to_f(elem)
        if comp.degree() <= annihilator_degree and comp * input_pol == 0:
            output.append(comp)
    return output

""" mistake in lecture notes, he is missing x1x2x3x4 from the example"""
states, x_vars = create_possible_states(x_vars)
F_truth_col = [F(elem) for elem in x_vars]
f = C_to_f(F_truth_col)

G0_truth = annihilators_truth_table(F_truth_col)
G0 = valid_annihilators(G0_truth, f)

F_xor_one = [(a+1)%2 for a in F_truth_col]
f_one = C_to_f(F_xor_one)
G1_truth = annihilators_truth_table(F_xor_one)
G1 = valid_annihilators(G1_truth, f_one)


print(f"{B}")
print(f"Boolean function F    := {f}")
print(f"G0 Annihilators of F  := {G0}")
print(f"G1 Annihilators of F  := {G1} ")