def generate_binary_vectors(n):
    """
    Generates all 0-1 vectors of length n in lexicographic order.
    :param n: Length of the vectors
    """
    vec = []
    for i in range(2**n):
        vec.append( [int(bit) for bit in format(i, f'0{n}b')] )
        
    return vec
    
def is_subset(n,i,j):
    """
    Checks whether A_j is a subset of A_i
    """
    v = generate_binary_vectors(n)
    for k in range(n):
        if v[j][k] > v[i][k]:
          return False
          
    return True
    
def set_minus(n,i,j):
    """
    Returns A_i \ A_j as a vector
    """
    v = generate_binary_vectors(n)
    diff_vector = []
    for k in range(n):
        if  v[i][k] == 1 and v[j][k] == 1:
            diff_vector.append(0)
        else:
            diff_vector.append(v[i][k])
    return diff_vector
    
def num_of_nonzeros(v):
    """Returns the non-zero elements of v
    """
    s = 0
    for i in range(len(v)):
        if v[i] != 0:
            s += 1
    return s
    
def generate_D(n):
    """
    Generates the matrix D. 
    """
    v = generate_binary_vectors(n)
    D = []
    
    for i in range(2**n):
        row = []
        for j in range(2**n):
            # Df_i(A_j)
            if (not is_subset(n,j,i)):
                row.append(0)
            else:
                row.append( (-1)**num_of_nonzeros(set_minus(n,j,i)) )
        D.append(row)
    return D        

def print_D(n):
    """
    Prints the rows of the matrix D of a given size
    """
    D = generate_D(n)
    for row in D:
        print(row)
        
def print_D_in_Mathematica_Form(n):
    """
    The same as print_D, but prints the matrix such that it is copiable to Mathematica directly
    """
    D = generate_D(n)
    print("{", end="")
    for row in D:
        print("{" + ", ".join(map(str, row)) + "},",end="")
    print("\b}")


n = 3
print_D_in_Mathematica_Form(n)
