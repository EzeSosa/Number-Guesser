#IMPORTO LAS LIBRERÍAS
from tkinter import *
from random import *

#RAÍZ
root = Tk()
root.title("Adivina el número!")
root.resizable(0, 0)

#VARIABLES
avisoNum = StringVar()
numGuess = StringVar()
intentos = 0
num = randrange(0, 100)

#FRAME
fram = Frame(root)
fram.config(width=400, height=150)
fram.pack()

#FUNCIONES
def adivinar():
    try:
        cad = ctext.get()
        cad = int(cad)

        if cad < 0 or cad > 100:
            avisoNum.set("¡EL RANGO ES 0-100!")

        else:
            if cad == num:
                avisoNum.set("¡NÚMERO ADIVINADO!")
                ctext["state"] = "disabled"
                label2["text"] = f"Intentos: {intentos + 1}"
                label3["text"] = f"Número intentado: {cad}"
                adiv["state"] = "disabled"
                aumenta_intentos()

            elif cad < num:
                avisoNum.set("¡EL NÚMERO ES MAYOR!")
                label2["text"] = f"Intentos: {intentos + 1}"
                label3["text"] = f"Número intentado: {cad}"
                aumenta_intentos()

            elif cad > num:
                avisoNum.set("¡EL NÚMERO ES MENOR!")
                label2["text"] = f"Intentos: {intentos + 1}"
                label3["text"] = f"Número intentado: {cad}"
                aumenta_intentos()

    except:
        avisoNum.set("¡TIPEA UN NÚMERO!")

    finally:
        numGuess.set("")

def aumenta_intentos():
    global intentos
    intentos += 1

#BOTÓN
adiv = Button(fram)
adiv.config(text="Adivinar", cursor="hand2", command=lambda:adivinar())
adiv.place(x=170, y=100)

#ENTRYs
aviso = Entry(fram)
aviso.config(state="disabled", textvariable=avisoNum, font=("Calibri", 15), width=21, justify="center")
aviso.place(x=170, y=50)

ctext = Entry(fram, textvariable=numGuess)
ctext.place(x=170, y=20)

#LABELs
Label(fram, text="Rango: 0 - 100").place(x=10, y=20)
Label(fram, text="Author: GitHub/EzeSosa").place(x=265, y=130)

label2 = Label(fram, text=f"Intentos: {intentos}")
label2.place(x=10, y=40)

label3 = Label(fram, text=f"Número intentado:")
label3.place(x=10, y=60)

root.mainloop()