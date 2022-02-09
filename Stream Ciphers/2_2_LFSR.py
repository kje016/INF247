# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
import Matrix_HF
import numpy as np
LFSR_taps = 2
fx = [41, 3, 0]        #x^41 + x^3 + x^0
lfsr_states = list(reversed([x for x in range(max(fx))]))

# give input_fx as decreasing powers of the function
def fx_to_cn(input_fx):
    fx = sorted(input_fx, reverse=True) #incase input_fx is not in a descending order
    Cn = [0]*max(input_fx)
    fx.pop(0)
    for i in fx:
        Cn[-(i+1)] = 1
    return Cn


def create_companion_matrix(lfsr_cn):
    companion_matrix = np.ndarray(shape=(len(lfsr_cn), len(lfsr_cn)), dtype=int)
    companion_matrix.fill(0)
    for i, elem in enumerate(companion_matrix):
        companion_matrix[i][0] = lfsr_cn[i]
        if not (i == len(lfsr_cn) - 1):  # fills in 1's on the diagonal, except for the last row (except for the Cn column)
            companion_matrix[i][i + 1] = 1
    return companion_matrix



def clock_lfsr(companion_matrix, lfsr_bool, clocks):
    #lecture notes p.43
    res_matrix = np.linalg.matrix_power(companion_matrix,clocks)
    res_matrix = Matrix_HF.matrix_mod2(res_matrix)
    matrix_col_prod = res_matrix.dot(lfsr_bool)

    # matrix_col_prod is a list from [0,...,40], however S_vector is defined as [40,...,0]
    # result_s_list is matrix_col_prod translated to [40,...,0]
    result_s_list = []
    for i in range(len(matrix_col_prod)):
        if matrix_col_prod[i] == 1:
            result_s_list.append(lfsr_states[i])
    return result_s_list


lfsr_cn = fx_to_cn(fx)
comp_matrix = create_companion_matrix(lfsr_cn)
clock_lfsr(comp_matrix, lfsr_cn, 1)
print(lfsr_cn)



""" Characteristic polynomial"""

def create_A(n, cn):
    companion_matrix = np.ndarray(shape=(n, n), dtype=int)
    companion_matrix.fill(0)
    for i, elem in enumerate(companion_matrix):
        companion_matrix[i][n-1] = cn[i]
        if not (i == n - 1):  # fills in 1's on the diagonal, except for the last row (except for the Cn column)
            companion_matrix[i][i + 1] = 1

    breakpoint()
    print("STOPITNOW")


n = 4
cn = [0]*n
cn[2], cn[3], cn[4] = 1, 1, 1
create_A(n,cn)



