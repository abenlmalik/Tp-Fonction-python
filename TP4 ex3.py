def permute():
    global A, B
    A, B = B, A
A=5
B=10
permute()
print("Après permutation : A =", A, "B =", B)
