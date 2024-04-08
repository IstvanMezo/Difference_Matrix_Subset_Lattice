import itertools
import numpy as np
from gen_D import generate_D


def construct_alternating_diagonal(n):
    # Create a diagonal matrix with +1 and -1 elements
    # This is the diagonal matrix we compare the commutator [D,X] with
    
    matrix = np.zeros((2**n, 2**n), np.int8)

    # Fill the diagonal with +1 and -1 elements
    for i in range(2**n):
        if i < 2**n // 2:
            matrix[i, i] = 1  # +1 on the diagonal
        else:
            matrix[i, i] = -1  # -1 on the diagonal

    return matrix

def is_alternating_diagonal(n, A):
    # Check if matrix A is alternating diagonal
    # i.e., of the form (1,1,...,-1,-1,...)

    return np.array_equal(A, construct_alternating_diagonal(n))

# Total number of possible n x n lower triangular matrices with zeros and minus ones.
def num_of_matrices(n):
    return 2**(n*(n+1)//2)
    
#Generates all possible n x n lower triangular matrices with zeros and minus ones.
def generate_all_lower_triangular_matrices(n):
    matrices = []

    for i in range(num_of_matrices(n)):
        binary_str = format(i, f'0{n*(n+1)//2}b')  # Convert i into binary string
        matrix = np.zeros((n, n), dtype=int)

        idx = 0
        for row in range(n):
            for col in range(row + 1):
                matrix[row, col] = int(binary_str[idx]) - 1
                idx += 1

        matrices.append(matrix)

    return matrices

#Puts the matrix M into the lower-left corner of a new, otherwise zero matrix of size 2**n times 2**n.
#Sizes are not checked, this is designed to be an internal function
def enlarge(n, M):

    matrix = np.zeros((2**n, 2**n), np.int8)

    for i in range(2**n // 2):
        for j in range(2**n // 2):
            matrix[2**n // 2 + i, j] = M[i, j]

    return matrix

#Final task: generate all the X matrices that satisfy the commutator relation by selection process
#To reduce the size of the problem, we consider only those Xs which are zero everywhere except the lower-left quarter
def generate_X(n):
    potentialXs = generate_all_lower_triangular_matrices(2**(n-1))
    ProperX = []
    D = generate_D(n)
    
    for i in range(num_of_matrices(2**(n-1))):
        #Enlarge PotentialXs[i] to a matrix of size 2**n times 2**n, and transpose it
        #These simplifications are necessary, because the sizes get too large
        #Transposition is based on a theoretical conjecture. Plus we did not find and X with untransposed minor matrix
        X = enlarge(n, np.transpose(potentialXs[i]) )

        #Check if potentialXs[i] satisfies the commutator relation. If yes, append it to the ProperX list
        commutator = np.dot(D, X) - np.dot(X, D)
        if is_alternating_diagonal(n, commutator):
            ProperX.append(X)
        
    print("\n")
    return ProperX


n = 3

print("The upper difference matrix D for n  = ", n, ":")
print(generate_D(n))

Xs = generate_X(n)

print("We have found these X matrices: ")
for matrix in Xs:
    for row in matrix:
        print(row)
    print("\n")
