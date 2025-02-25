a = int(input("Entrez le premier nombre: "))
b = int(input("Entrez le deuxiéme nombre: "))
c = int(input("Entrez le deuxiéme nombre: "))
d = int(input("Entrez le deuxiéme nombre: "))
#mini = lambda a, b: a if a < b else b
#print(mini(a,b))
def minimum(x,y,z,v):
    min_nombre = min(min(x,y),min(z,v))
    print(f"Le minimum est:{min_nombre}")
minimum(a,b,c,d)