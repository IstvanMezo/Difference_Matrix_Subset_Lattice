import itertools
import numpy as np
from gen_D import generate_D


#Show percent for longer calculations. Taken from here:
#https://realpython.com/python-print/#building-console-user-interfaces
def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

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

def generate_X(n):
    # Generate all possible combinations of 0s and (-1)s for the lower triangular part
    num_of_positions = (2**n)*((2**n)-1)//2
    num_of_matrices = 2**num_of_positions
    combinations = list(itertools.product([0, -1], repeat= num_of_positions))

    ProperX = []
    D = generate_D(n)
    print("\nNow generating Xs. There are ",  num_of_matrices, " possible cases...")
    progress(0)
    
    # Iterate over each combination
    iter = 0 # Count the states for user feedback in progress()
    for combo in combinations:
        # Create an empty 2**n x 2**n matrix
        matrix = [[0] * 2**n for _ in range(2**n)]

        # Fill the lower triangular part with the values from combinations
        idx = 0
        for i in range(2**n):
            for j in range(0, i):
                matrix[i][j] = combo[idx]
                idx += 1

        #Check if "matrix" satisfies the commutator relation. If yes, append to ProperX
        commutator = np.dot(D, matrix) - np.dot(matrix, D)
        if is_alternating_diagonal(n, commutator):
            ProperX.append(matrix)
        
        #Feedback to the user
        iter += 1
        progress(int((iter / num_of_matrices) * 100))

        
    print("\n")
    return ProperX


n = 2

print("The upper difference matrix D for n  =", n, ":")
print(generate_D(n))

Xs = generate_X(n)

print("We have found these X matrices: ")
for matrix in Xs:
    for row in matrix:
        print(row)
    print("\n")
