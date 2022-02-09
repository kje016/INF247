# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
from sage.all import *
from copy import deepcopy

""" How many key_stream bits are needed for"""
"""This is code for the example in lecture notes p.66"""
var('x')

d = 2       # d := algebraic degree of F
n = 4       # n := algebraic degree of feedback
D = 0

for i in range(n):
    var(str(s)+str(i))
R = PolynomialRing(GF(2), 's')

feedback_f = x**4 + x + x**0
state_feedback = [b for a, b in feedback_f.coefficients()]
state_feedback.pop()

# upper bound on linear complexity
for i in range(d+1):
    D = D + binomial(n, i)

def s_to_vec(s):
    output_vec = [0]*D
    string = [0] * n
    breakpoint()
    if type(s) is int:
        string[s] = 1
        index = Integer(''.join([str(elem) for elem in string[::-1]]), base=2)
        output_vec[index] = 1
    else:
        for a in s:
            string[a] = 1
            index = Integer(''.join([str(elem) for elem in string]), base=2)
            output_vec[index] = 1
    return output_vec




""" Comptuing S(t)"""
s_t = list(range(n-1, -1, -1))
comp_list = []
for i_a, a in enumerate(s_t):
    if i_a == len(s_t)-1:
        break
    rest_list = s_t[i_a+1:]
    rest_list.reverse()
    for b in rest_list:
        comp_list.append([a, b])
s_t.extend(comp_list)
s_t.insert(0, 1)
print(s_t)

""" Computing S(t+1)"""
s_t1 = deepcopy(s_t)
s_t1.remove(0)
s_t1.insert(1, list(state_feedback))
for elem in range(n+1, len(s_t1)):
    for i, state in enumerate(s_t1[elem]):
        if type(s_t1[elem]) == int:
            continue
        if state == n-1:
            s_t1[elem][i] = state_feedback
        else:
            s_t1[elem][i] += 1

print()
print(f"s_t := {s_t}")
print(f"s_tq := {s_t1}")


def create_R(st):
    output_mat = []
    output_mat.append([1]+[0]*(D-1))
    for i in range(1, len(st)):
        output_mat.append(s_to_vec(st[i]))


#R = create_R(s_t)
A = MatrixSpace(IntegerRing(), 11)([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]])
f = A.charpoly()

