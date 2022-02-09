# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
from sage.all import *
from math import log2


F_col = [0, 0, 1, 1, 1, 0, 0, 1]
xn = int(log2(len(F_col)))
F_col_lexicographical = []

for i in range((2**xn)):
    bit = "{0:b}".format(i)
    padding = "0" * (xn-len(bit))
    bit_string = padding + bit
    F_col_lexicographical.append([x for x in bit_string])


def Walsh_Hadamard_Transform(truth_col):
    WH = []
    WH_len = int(log2(len(truth_col)))
    # Initialize W0,a = (-1) ^(F(a))
    for i in truth_col:
        WH.append((-1)**i)

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


def fast_WH(truth_col):
    WH = []
    for i in truth_col:
        WH.append((-1) ** i)

    WH_len = int(log2(len(truth_col)))
    for i in range(WH_len):
        vector_len = 2 ** i
        for j in range(0, len(WH), 2 ** (i + 1)):
            fst_half = range(j, j + (vector_len - 1) + 1)
            snd_half = range(j + (vector_len), j + (2 * (vector_len) - 1) + 1)

            fst_half = [i for i in fst_half]
            snd_half = [i for i in snd_half]
            for k in range(len(fst_half)):
                orig_val = WH[fst_half[k]]
                WH[fst_half[k]] = WH[fst_half[k]] + WH[snd_half[k]]
                WH[snd_half[k]] = orig_val - WH[snd_half[k]]

    best_AA = []  # The best affine approximation(s)
    prob_WH = []  # Probabilities of each affine function 'g'=F
    for i in range(len(WH)):
        if WH[i] == 0:
            continue
        else:
            if WH[i] > 0:
                best_AA.append(F_col_lexicographical [i])
                prob_WH.append((1 + (abs(WH[i]) / len(WH))) / 2)
            else:
                best_AA.append([F_col_lexicographical[i], '1'])
                prob_WH.append((1 + (abs(WH[i]) / len(WH))) / 2)
    return WH, best_AA, prob_WH


transform, best_approximation, prob_approx = fast_WH(F_col)
print(f"F truth column := {F_col}")
print(f"Walsh Hadarmard Transform := {transform}")
print(f"best approximation := {best_approximation}")
print(f"their approximation:= {prob_approx}")
