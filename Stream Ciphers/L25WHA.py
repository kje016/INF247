# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
# WHA := Walsh Hadamard transform Applications
from sage.all import *

N = [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0]
var('x')

feed_back_func = [3, 4]
lfsr_func = [0, 1, 3]
lfsr_len = 4


def F(input_list):
    x1, x2, x3, x4 = input_list
    func = x1*x2 +x4
    return func

def comp_matrix(feedback):
    mat = []
    co_row = [0]*lfsr_len
    for elem in feedback:
        co_row[elem-1] = 1
    mat.append(co_row)
    for i in range(lfsr_len-1):
        row = [0]*lfsr_len
        row[i] = 1
        mat.append(row)
    return Matrix(GF(2), mat)

def create_b():
    b = []
    state_vec = [0]*lfsr_len
    state_vec[-1] = 1
    state_vec = vector(GF(2), state_vec)
    for i in range(len(N)):
        b.append(state_vec*A**i)
    return b

def lexicographical(b):
    lexi_order = []
    for elem in b:
        b_str = ''.join([str(c) for c in elem])
        lexi_order.append(int(b_str, 2))
    return lexi_order

A = comp_matrix(feed_back_func)
B = create_b()
B_lexicographical = lexicographical(B)
min_zi = [(-1)**zi for zi in N]


def create_vec_C():
    c_vec = []
    for i in range(0, 2**lfsr_len):
        try:
            c_vec.append((-1)**N[B_lexicographical.index(i)])
        except:
                c_vec.append(0)
    return c_vec

def Walsh_Hadamard_Transform(truth_col):
    WH = truth_col
    WH_len = log(len(truth_col), 2)

    for i in range(WH_len):
        vector_len = 2 ** i
        for j in range(0, len(WH), 2 ** (i + 1)):
            fst_half = range(j, j + (vector_len - 1) + 1)
            snd_half = range(j + vector_len, j + (2 * vector_len - 1) + 1)

            fst_half = [i for i in fst_half]
            snd_half = [i for i in snd_half]
            for k in range(len(fst_half)):
                orig_val = WH[fst_half[k]]
                WH[fst_half[k]] = WH[fst_half[k]] + WH[snd_half[k]]
                WH[snd_half[k]] = orig_val - WH[snd_half[k]]
    return WH

C = create_vec_C()
W = Walsh_Hadamard_Transform(C)
N1x = [int(((len(N)-wx) / 2)) for wx in W]

print(N1x)

candidates = [i for i, a in enumerate(N1x) if a/len(N) <= 1.5/4]
candidates = [B[B_lexicographical.index(i)] for i in candidates]
print(candidates)



breakpoint()

