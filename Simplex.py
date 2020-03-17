#Metodo Simplex con tres ecuaciones a dos variables

import math

print(" ------------------------------ ")
print("| METODO SIMPLEX DOS VARIABLES |")
print(" ------------------------------ ")
print(" ")

mSimplex=[]

iEcua= int(input("Ingrese cantidad de inecuaciones "))
iVar = int(input("Ingrese cantidad de variables "))

iCOl=iEcua+iVar+3
iFil=iEcua+2

for i in range(iFil):
    mSimplex.append([])
    for f in range(iCOl):
        mSimplex[i].append(None)

for i in range(1,iFil):
    if i < iFil-1:
        pass
        mSimplex[i][0]="S"+str(i)
    if i==iFil-1:
        mSimplex[i][0]="Z"

for i in range(1,iCOl):
    if i==1:
        mSimplex[0][i]="Z"
    if i<=iVar+1 and i > 1:
        mSimplex[0][i]="X"+str(i-1)
    if i<iCOl and i > iVar+1:
        mSimplex[0][i]="S"+str(i-iVar-1)
    if i==iCOl-1:
        mSimplex[0][i]="B"

for i in range(1,iCOl):
    if i==1:
        mSimplex[iFil-1][i]=1
    elif i>1 and i<iVar+2:
        mSimplex[iFil-1][i]=int(input("Ingrese variable "+str(i)+"° de la funcion objetivo  "))*(-1)
    else:
        mSimplex[iFil-1][i]=0

cvar=0
cecua=0
q=0
for i in range(1,iFil-1):
    cecua=cecua+1
    for j in range(1,iCOl):
        cvar=cvar+1
        if j==1:
            mSimplex[i][j]=0
        if j<iVar+2 and j>1:
            mSimplex[i][j]=int(input("Ingrese valor "+str(cvar)+"° de la "+str(cecua)+"° inecuación "))
        if j>iVar+1 and j<iCOl-1:
            if q < j:
                q=j
            mSimplex[i][q]=1
            for k in range(j+1,iCOl-1):
                mSimplex[i][k]=0
                q=q+1






for i in range(iFil):
    print("")
    for f in range(iCOl):
        print(""+str(mSimplex[i][f]),end='      ')