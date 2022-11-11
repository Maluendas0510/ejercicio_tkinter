#Se importa libreria tkinter con todas sus funciones

from tkinter import *
from tkinter import messagebox

# funciones de la app



def sumar():
    messagebox.showinfo("Suma 1.0", "Hizo clic en el boton sumar...")

    c1=int(x.get())%10
    c2= ((int(x.get())%100)-c1)//10
    S=c1+c2
    if S < 10:
        cifras = 1
    else:
        cifras=2
    t_resultados.insert(INSERT, "La suma de los ultimos dos digitos del numero " + str(x.get()) + " es un numero de " + str(cifras) + " cifras."+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos seran borrados...")
    x.set("")
    
    t_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrara...")
    ventana_principal.destroy()

# variables globales 



#ventana principal

#se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Sistemas UIS")

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("500x500")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="black")

x = StringVar()
#--------------------
#frame entrada datos
#--------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "white", width = 480 , height = 240)
frame_entrada.place(x = 10, y = 10)



#Logo de la app
#logo = PhotoImage(file = "img/suma.png")
#lb_logo = Label(frame_entrada, image = logo)

# Etiquetas par el titulo de app
titulo = Label(frame_entrada, text = "Suma de los dos ultimos digitos de un numero. ")
titulo.config(bg = "white", fg = "blue", font = ("Arial",16))
titulo.place(x = 20, y = 10)

# Etiqueta para x
lb_numero = Label(frame_entrada, text = "Ingrese el numero = ")
lb_numero.config(bg="white", fg="blue", font=("Arial",16))
lb_numero.place(x=100, y=50)

# Entry para x
entry_numero= Entry(frame_entrada, textvariable=x)
entry_numero.config(font=("Arial",20), justify=LEFT,fg="blue")
entry_numero.focus_set()
entry_numero.place(x=300, y=50, width=115, height=30)




#--------------------
#frame operaciones
#--------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "white", width = 480 , height = 120)
frame_operaciones.place(x = 10, y = 260)

# Boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar", command=sumar)
bt_sumar.place(x=45, y=45, width=100, height=30)

#Boton borrar
bt_sumar = Button(frame_operaciones, text="Borrar")
bt_sumar.place(x=190, y=45, width=100, height=30)

#Boton borrar
bt_sumar = Button(frame_operaciones, text="Borrar",command=borrar)
bt_sumar.place(x=190, y=45, width=100, height=30)

# Boton salir
bt_salir = Button(frame_operaciones, text="Salir",command=salir)
bt_salir.place(x=335, y=45, width=100, height=30)

# fram resultados

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=100)
frame_resultados.place(x=10, y = 390)

#area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="green", fg="black", font=("Arial",14))
t_resultados.place(x=10,y=10, width=460, height= 80)

ventana_principal.mainloop()