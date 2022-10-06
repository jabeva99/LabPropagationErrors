import tkinter as tk
from tkinter import filedialog,Text,messagebox,ttk
import os
import sympy as sym
import numpy as np
import pandas as pd
import math as mt

loc=""
vars=[]
func=""
seleccion=""
root=tk.Tk()
canvas=tk.Canvas(root,height=550,width=900,bg="#263D42")
canvas.pack()


entryfile=tk.Entry(root)
canvas.create_window(300,50,window=entryfile)
def getloc():
    global loc
    loc=entryfile.get()
    print(loc)

buttonfile=tk.Button(root, height=1, width=18, text="Añadir nombre fichero", command=lambda:getloc())

canvas.create_window(300,100,window=buttonfile)


entryvar=tk.Entry(root)
canvas.create_window(700,50,window=entryvar)
def getvars():
    global vars
    vars.append(sym.Symbol(entryvar.get()))

    entryvar.delete(0,tk.END)
buttonvar=tk.Button(root, height=1, width=15, text="Añadir variable", command=lambda:getvars())

canvas.create_window(700,100,window=buttonvar)



entryfunc=tk.Entry(root)
canvas.create_window(300,250,width=400,window=entryfunc)
#entryfunc.pack()
def getfunc():
    global func
    func=entryfunc.get()
    print(func)

buttonfunc=tk.Button(root, height=1, width=15, text="Añadir funcion", command=lambda:getfunc())

canvas.create_window(300,300,window=buttonfunc)







combo=ttk.Combobox(state="readonly")

opciones=["csv","excel"]
def lista_selec():
    global seleccion
    seleccion=combo.get()
    print(seleccion)

canvas.create_window(700,250,window=combo)


combo['values']=opciones

buttonfich=tk.Button(root, height=1, width=15, text="Añadir formato", command=lista_selec)

canvas.create_window(700,300,window=buttonfich)


def execute():
    root.quit()
    root.withdraw()




# Button for execute
exit_button = tk.Button(root, text="Ejecutar", command=execute)
canvas.create_window(450,450,window=exit_button)








root.mainloop()


nvar=len(vars)

if seleccion=="excel":

    df = pd.read_excel(str(loc))

if seleccion=="csv":

    df = pd.read_csv(str(loc))







funval=[]

errores=[]
for j in range(int(df.shape[0])):

    datosexp=[]
    datoserr=[]

    for i in range(int(len(df.columns)*0.5)):
        datosexp.append(df.iat[j,2*i])
        datoserr.append(df.iat[j,2*i+1])

    derivadas=[]
    for i in vars:
        derivadas.append(sym.diff(func,i))
    print(derivadas)

    devnum=[]

    tuplaexp=[]

    for i in range(len(datosexp)):
        tuplaexp.append((vars[i],datosexp[i]))


    funval.append(sym.sympify(func).subs(tuplaexp))




    for i in derivadas:
        devnum.append(i.subs(tuplaexp))
    print(devnum)
    devnumerr=[]
    cont=0
    for i in devnum:
        devnumerr.append((i*datoserr[cont])**2)
        cont+=1
    errores.append(mt.sqrt(sum(devnumerr)))

print(errores)

df['f']=funval

df['Df']=errores

if seleccion=="excel":
    df.to_excel("output.xlsx")

if seleccion=="csv":
    df.to_csv("output.csv")


