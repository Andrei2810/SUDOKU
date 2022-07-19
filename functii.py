f=open("input.txt","r")
mat = [[0 for i in range(9)] for j in range(9)]
def citire():
    mat = [[0 for i in range(9)] for j in range(9)]
    linie=[]
    n=int(f.readline())
    if n==-1:
        return "Nu mai aveti ce sa cititi din fisier"
    for i in range(n):
        linie=f.readline().split()
        x=int(linie[0])
        y=int(linie[1])
        val=int(linie[2])
        mat[x][y]=val
    return mat
def afisare_solutie():
    for i in range(9):
        for j in range(9):
            print(mat[i][j],end=' ')
        print(" ")
def citire_tastatura():
    mat = [[0 for i in range(9)] for j in range(9)]
    n = int(input("Introduceti numarul de elemente nenule din tabel "))
    for i in range(n):
        x =int(input("Introduceti linia x din matrice"))
        y =int(input("Introduceti coloana y din matrice"))
        val =int(input("Introduceti linia val din matrice"))
        mat[x][y] = val
    return mat

