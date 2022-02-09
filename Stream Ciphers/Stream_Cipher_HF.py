from math import log2
def string_to_list(input_string):
    return [int(x) for x in input_string]

#creates all possile initial states of lfsr register of length n
# ordered lexicographically rising
def create_possible_states(list_len):
    output_list = []
    x_n = []
    for i in range((2**list_len)):
        bit = "{0:b}".format(i)
        padding = "0" * (list_len - len(bit))
        bit_string = padding + bit
        x_n.append([x for x in bit_string])
        output_list.append(bit_string)
    return output_list, x_n

list, x1_n = create_possible_states(5)

# F = boolean function
def F(input_list):
    if type(input_list) is str:
        input_list = [int(x) for x in input_list]
    x1, x2, x3, x4, x5 = input_list
    return ((x1 * x2) ^ x3 ^ x4 ^ x5)

def bool_func_col(input_registers):
    output_list = []
    for register in input_registers:
        output_list.append(F(register))
    return output_list

tess = bool_func_col(list)

print("STOP")



def Walsh_Hadamard_Transform(truth_col):
    WH = []
    WH_len = log(len(truth_col), 2)
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

def get_best_AA(wh_transform, x_n):
    best_AA = []
    prob_WH = []
    for i in range(len(wh_transform)):
        if wh_transform[i] == 0:
            continue
        else:
            if wh_transform[i] > 0:
                best_AA.append(x_n[i])
                prob_WH.append((1 + (abs(wh_transform[i]) / len(wh_transform))) / 2)
            else:
                best_AA.append([x_n[i], '1'])
                prob_WH.append((1 + (abs(wh_transform[i]) / len(wh_transform))) / 2)

    return best_AA, prob_WH

