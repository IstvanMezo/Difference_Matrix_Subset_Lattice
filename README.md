# Difference_Matrix_Subset_Lattice
The program gen_D.py generates the upper-difference matrix of the subset lattice for a particular basis.
For a given n, this basis consists of 2^n functions f_0, f_1,..., and they are defined by the relation f_i(A_j)=Kronecker_{i,j}.
Here A_j is a subset of S={1,...,n}, and it is defined to be the "characteristic function" of the binary representation of j (j=0,1,...,2^n-1).
For example, if n=3, and j = 3, then 3=0*2^2+1*2^1+1*2^0, so A_3={1,2}. A_0 is the empty set.

The output is printed by print_D(n), where n is the size of the base set S.
The function print_D_in_Mathematica_Form(n) does the same, but the output is directly copiable into a Mathematica worksheet.

(The '\b' character in print_D_in_Mathematica_Form(n) works properly on Linux terminal, but not with some online interpreters.)

To use the program, set n for the printing function inside the code, and type
python3 gen_D.py from its directory.
Or copy the source code into an online Python interpreter.

The program gen_X.py generates the (or those) X matrices of size 2^n times 2^n for which the commutator [D,X] = diag(1,1,...,-1,-1,...) (half of the elements is +1, the other half is -1).

These codes are for a mathematical (lattice-theoretical) project. For more details, see our future paper (announced here when it gets available ;))

Notice: I could only make it run for n = 1,2 (lack of resources? Working on it...)
