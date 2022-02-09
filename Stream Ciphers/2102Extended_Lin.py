# cd Desktop/V21/INF247/ExamPrep/'Stream Ciphers'
from sage.all import *
from sage.crypto.boolean_function import BooleanFunction

x_vars = 3
var('x')
B = BooleanPolynomialRing(x_vars, 'x'); B
B.inject_variables()

f0 = x0*x1 + x2
f1 = x1*x2 + x2 + x0
f2 = x0*x2 + x1

M = Matrix(B, [[f0, 0],[f1, 1], [f2, 0]])

#original_polynomials = [f0, f1, f2]
#polynomials = original_polynomials[:]

def extend_mat(mat):
    output_mat = []
    for row in mat:
        for var in B.variable_names():
            output_mat.append(row*B(var))
    return Matrix(B, output_mat)


def linearize_matrix(input_mat):
    lin_matrix = []
    lin_variables = {}
    var_getter = x_vars
    """Linearize matrix"""
    for row in input_mat:
        #breakpoint()
        new_row = []
        for pol in row:
            terms = pol.terms()
            if not terms or pol.degree() < 1:
                new_row.append(row[-1])
                continue
            for term in pol.terms():
                if term.degree() > 1:
                    new_var = str(x)+str(var_getter)
                    dict_getter = (lin_variables.get(term, None))
                    if dict_getter == None:
                        new_row.append(new_var)
                        lin_variables.update({term: new_var})
                        var_getter += 1
                    else:
                        new_row.append(dict_getter)
                else:
                    new_row.append(str(term))
                #breakpoint()
            #new_row.append(new_pol)
        lin_matrix.append(new_row)       # flattening the 2d-list new_row

    """ turn 2d_array to sagemath Matrix"""
    breakpoint()
    R = BooleanPolynomialRing(var_getter, 'x'); R
    R.inject_variables()
    for i_row, row in enumerate(lin_matrix):
        lin_matrix[i_row] = [sum([R(a) for a in row])]

    breakpoint()
    return lin_matrix


#polynomials.append([a*B(var) for a in original_polynomials for var in B.variable_names()])

extended_matrix = extend_mat(M)
extended_matrix = M.stack(extended_matrix)
lin_matrix = linearize_matrix(extended_matrix)
breakpoint()


