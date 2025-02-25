def logarithme(a):
   
    n=0
    while 2**n <= a:
        n = n+1
    return n
x = int(input("Entrer un nombre:"))
print("n=",logarithme(x))