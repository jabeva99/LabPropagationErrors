import sympy as sym
import numpy as np
import math as mt

nval=inpunval=int(input("Introduce el numero de variables  "))
print("Introduce las variables una a una  ")
vals=[]
for i in range(nval):
    a=input("")
    vals.append(sym.Symbol(a))

print(vals)

print("Introduce la funcion del error")

f=input()

derivadas=[]
for i in vals:
    derivadas.append(sym.diff(f,i))
print(derivadas)

devnum=[]

X=5
dx=0.2
Y=10
dy=10


for i in derivadas:
    devnum.append(i.subs([(vals[0],5),(vals[1],4)]))
print(devnum)

