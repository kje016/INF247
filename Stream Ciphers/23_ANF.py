# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
from sage.all import *
from functools import reduce
field = GF(2);
var('x')
var('x1')
var('x2')
var('x3')
var('x4')
f = vector(GF(2), [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1])
n = log(len(f),2)


def Kronecker_Product(base_matrix, current_matrix):
    dim = current_matrix.nrows() * 2
    G1N = MatrixSpace(field, dim)
    G2N = MatrixSpace(field, dim)
    G3N = MatrixSpace(field, dim)
    G4N = MatrixSpace(field, dim)

    G1N = matrix([base_matrix[0, 0] * g for g in current_matrix])
    G2N = matrix([base_matrix[0, 1] * g for g in current_matrix])
    G3N = matrix([base_matrix[1, 0] * g for g in current_matrix])
    G4N = matrix([base_matrix[1, 1] * g for g in current_matrix])

    result_matrix = block_matrix([[G1N, G2N], [G3N, G4N]])
    return result_matrix


def comp_A():
    A1 = matrix(GF(2), [[1, 1], [0, 1]])
    GN = Kronecker_Product(A1,A1)
    for i in range(1, n-1):
        GN = Kronecker_Product(A1, GN)
    return GN


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


# Important to check if amountof variables is correct
def truthcol_to_var(lexi_string):
    pol = [x1*lexi_string[0], x2*lexi_string[1], x3*lexi_string[2], x4*lexi_string[3]]
    output = 1*x**0
    for elem in pol:
        if elem != 0:
            output = output*elem
    return output


def C_to_f(c):
    n_vars = log(len(c), 2)
    _, lexi_vars = create_possible_states(n_vars)
    f = 0*x**0
    for i, elem in enumerate(c):
        if elem == 1:
            f = f+(truthcol_to_var(lexi_vars[i]))
    print(f)
    return f



An = comp_A()
C = f*An
cf = C_to_f(C)
print(f"f  ={f}")
print(f"An =\n{An}")
print(f"C  = {C}")
print(f"cF = {cf}")


""" Fast ANF """
def fast_ANF(truth_col):
    WH = truth_col[:]
    WH_len = log(len(truth_col), 2)
    for i in range(WH_len):
        print(WH)
        vector_len = 2 ** i
        for j in range(0, len(WH), 2 ** (i + 1)):
            fst_half = range(j, j + (vector_len - 1) + 1)
            snd_half = range(j + (vector_len), j + (2 * (vector_len) - 1) + 1)

            fst_half = [i for i in fst_half]
            snd_half = [i for i in snd_half]
            for k in range(len(fst_half)):
                WH[snd_half[k]] = (WH[fst_half[k]] + WH[snd_half[k]])%2
    return WH
fast = fast_ANF(f)
C_fast = C_to_f(fast)
print(f"fast    := {fast}")
print(f"Cf_fast :={C_fast}")

