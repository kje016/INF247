# cd Desktop/V21/INF247/ExamPrep
from sage.all import *
import numpy as np
import copy
from functools import reduce

def companion_matrix(n, cn):
    companion_matrix = np.ndarray(shape=(n, n), dtype=int)
    companion_matrix.fill(0)
    for i, elem in enumerate(companion_matrix):
        companion_matrix[i][n - 1] = cn[i]
    for i in range(1,n):
        companion_matrix[i][i-1] = 1
    companion_matrix = matrix(GF(2), companion_matrix)
    return companion_matrix


companion_matrix(4, [1,0,0,1])

def matrix_mod2(input_matrix):
    result_matrix = input_matrix
    for i,elem in enumerate(input_matrix):
        result_matrix[i] = np.fmod(elem,2) #np.fmod()
    return result_matrix

# lfsr_cn := the lfsr given as a binary string


#tror det burde gjøres på en annen måte
def matrix_power_to(input_matrix, power):
    res_matrix = np.linalg.matrix_power(input_matrix, power)
    res_matrix = matrix_mod2(res_matrix)
    return res_matrix


def augment_matrix(U_matrix, Vk):
    copy_U = copy.deepcopy(U_matrix)
    for index in range(len(copy_U)):
        copy_U[index].append(Vk[index])
    return copy_U

"""Converts a matrix to reduced row echelon form (RREF)"""
def RREF(input_matrix):
    pivot_indecies = []
    m, n = input_matrix.rows(), input_matrix.cols()
    current_row = 0

    for j in range(n):
        if current_row >= m:
            break
        pivot_row = current_row
        while pivot_row < m and input_matrix[pivot_row, j] == 0:
            pivot_row += 1

        if pivot_row == m:
            continue

        input_matrix[[current_row, pivot_row]] = input_matrix[[pivot_row, current_row]]
        pivot_row = current_row
        current_row += 1
        for i in range(current_row, m):
            if input_matrix[i, j] == 1:
                input_matrix[i] = (input_matrix[i] + input_matrix[pivot_row]) % 2  # subtracting is same as adding in GF(2)

    for i in reversed(range(current_row)):
        # Find pivot
        pivot_col = 0
        # find the column with the first non-zero entry.
        while pivot_col < n and input_matrix[i, pivot_col] == 0:
            pivot_col += 1
        if pivot_col == n:
            continue  # Skip this all-zero row
        # Remove this column in all the rows above
        for j in range(i):
            if input_matrix[j, pivot_col] == 1:
                input_matrix[j] = (input_matrix[j] + input_matrix[i]) % 2
        pivot_indecies.append(pivot_col)

    return input_matrix, pivot_indecies

###########################################################################################################
""" This section is for solving a system of equations given an augmented matrix """
def get_variabel_coef2(matrix_row, relevant_variables, list_of_results):
    relevant_variables.pop(0)   #remove the variable we are trying to solve

    relevant_coefficients = []
    for i in relevant_variables:
        relevant_coefficients.append(list_of_results[i])
    result_coef = reduce(lambda x,y: x^y, relevant_coefficients)
    return (result_coef^matrix_row[-1])

def get_row_result2(input_row, list_of_results):
    relevant_variables = []
    for index in range( len(input_row)-1):
        if input_row[index] == 1:
            relevant_variables.append(index)
    if len(relevant_variables) == 1:
        method_result = input_row[-1]               #input_row[-1] is the right-hand side of the equation
        return method_result
    else:
        method_result = get_variabel_coef2(input_row, relevant_variables, list_of_results)
        return method_result



def solve_sys_lin_eq(input_matrix, pivot_indecies, list_of_results, i):
    if i == 0 :
        list_of_results[i] = get_row_result2(input_matrix[i], list_of_results)
        possible_lfsr_states.append(list_of_results[:])
        return
    try:
        row_index = pivot_indecies.index(i)
        list_of_results[i] = get_row_result2(input_matrix[row_index], list_of_results)
        solve_sys_lin_eq(input_matrix, pivot_indecies, list_of_results, i - 1)
        return
    except:
        list_of_results[i] = 0
        solve_sys_lin_eq(input_matrix,pivot_indecies,list_of_results, i - 1)

        list_of_results[i] = 1
        solve_sys_lin_eq(input_matrix,pivot_indecies,list_of_results, i - 1)
        return


def remove_all_0_rows(input_matrix):
    for i in range(len(input_matrix)-1,-1, -1):
        if all(x == 0 for x in input_matrix[i]):
            del input_matrix[i]
    return input_matrix

def is_consistent_matrix_w_o_0(input_matrix):
    last_row = input_matrix[-1]
    last_two_elems = last_row[-2:]
    if np.array_equal(last_two_elems, [0,1]):
        return False
    return True


""""
dummy_list is just used as as placeholder for inserting solutions as solve_sys_lin_eq()
When the method reaches the bottom of the recursion-tree, dummy_list is appended to possible_lfsr_states
to see solving system in effect check assignment 2, bottom of python file"""
dummy_list = [3]* 12 # [3] * 'len of lfsr'
possible_lfsr_states = []
##########################################################################################################