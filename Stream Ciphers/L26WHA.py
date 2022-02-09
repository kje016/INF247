# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
# WHA := Walsh Hadamard transform Applications
from sage.all import *
""" Most Biased linear functions"""
Pi = vector([1/2, 0, 0, 0, 1/6, 1/6, 0, 1/6])
n = 3
var('x')
for i in range(1,n+1):
    var(str(x)+str(i))


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


def Walsh_Hadamard_Transform(prob_vec):
    WH = prob_vec[:]
    WH_len = log(len(prob_vec), 2)

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


def find_best_candidates(wh):
    output = {}
    for i in range(1, len(wh)):
        getter = output.get(wh[i])
        if getter == None:
            output.update({wh[i] : [state_list[i]]})
        else:
            getter.append(state_list[i])
            output.update({wh[i]: getter})

    best_candidates = max(list(output.keys()))
    best_candidates = output.get(best_candidates)
    candidates_pos = [state_list.index(elem) for elem in best_candidates]
    return best_candidates, candidates_pos


def comp_prob(candidates):
    output = []
    for elem in candidates:
        comp = Pi[0] + (wh_transform[elem]/2)
        output.append(comp)
    return output


""""
str_state, state_list = create_possible_states(n)
wh_transform = Walsh_Hadamard_Transform(Pi)
vars_candidate, pos_candidates = find_best_candidates(wh_transform)
robabilities = comp_prob(pos_candidates)
print(f"wh_transform   := {wh_transform}")
print(f"wh best pos    := {pos_candidates}")
print(f"var candidates := {vars_candidate}")
print(f"probs          := {probabilities}")
"""


""" Vectorial Boolean functions and S-boxes """
n, m = 2, 2

_, S_vars = create_possible_states(n+m)


def valid_mappings():
    #TODO: calculate
    # now: taken from lecture
    return {(0, 0): [1, 0], (0, 1): [0, 1], (1, 0): [1, 1], (1, 1): [0, 0]}


def calc_prob_vec(ss):
    vec = []
    for elem in ss:
        x_vars = s_mappings.get(tuple(elem[:n]))
        if not x_vars == elem[n:]:
            vec.append(0)
        else:
            vec.append((1/(2*n)))
    return vec
def Walsh_Hadamard_Transform_alternate(prob_vec):
    WH = prob_vec[:]
    print(WH)
    WH_len = log(len(prob_vec), 2)

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
        print(WH, i)
    return WH

s_mappings = valid_mappings()
P = calc_prob_vec(S_vars)


#wh = [1 if x > 0 else 0 for x in P]        #in lecture notes *4 to make calculations in wh easier

wh = Walsh_Hadamard_Transform_alternate(P)
