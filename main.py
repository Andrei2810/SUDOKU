from functii import *


mat = [[0 for i in range(9)] for j in range(9)]
def cautare_linie(l,x):
    for i in range(9):
        if mat[l][i]==int(x):
            return False
    return True
def cautare_coloana(col,x):
    for i in range(9):
        if mat[i][col]==x:
            return False
    return True
def cautare_patrat(nlin,ncol,x):
    i0=nlin-nlin % 3
    j0=ncol-ncol % 3
    for di in range(3):
        for dj in range(3):
            if mat[i0+di][j0+dj]==x:
                return False
    return True
def validare(nlin,ncol,nr):
    if cautare_patrat(nlin,ncol,nr)==True and cautare_coloana(ncol,nr)==True and cautare_linie(nlin,nr)==True:
        return True
    else:
        return  False
def liber(t):
    for i in range(9):
        for j in range(9):
            if mat[i][j]==0:
                t[0]=i
                t[1]=j
                return t
    return False
def rezolva():
    coord=[0,0]
    if liber(coord)==0:
        return True
    else:
        i=coord[0]
        j=coord[1]
        for nr in range(1,10):
            if validare(i,j,nr)==1:
                mat[i][j]=nr
                if rezolva()==True:
                    return True
                mat[i][j]=0
        return False

while(1):
    print("1.Citire fisier : \n"
          "2.Afisare\n"
          "3.Rezolva sudoku\n"
          "4.Citire de la tastatura\n"
          "5.Informatii despre autor\n"
          "6.Iesire")
    opt=int(input("Introduceti optiunea "))
    if opt==1:
        mat=citire()
    elif opt==2:
        if (mat == "Nu mai aveti ce sa cititi din fisier"):
            print("Nu mai aveti ce sa cititi din fisier")
            f.close()
        else:
            for i in range(9):
                for j in range(9):
                    print(mat[i][j],end=' ')
                print()
    elif opt==3:
        if rezolva():
            print("Solutia este : ")
        else:
            print("Nu s-a putut gasi solutie ")
        for i in range(9):
            print(*mat[i])
    elif opt==4:
        mat=citire_tastatura()
    elif opt==5:
        print("Aluculesei Andrei Bogdan 3111b")
    elif opt==6:
        break




