from tkinter import *

cont = 1
lim = 5

def insereNumero(valor):
    global cont
    global lim
    if cont <= lim:
        eval('num' + str(cont) + '.set(' + valor + ')')
        cont += 1
    else:
        num1.set("Chega!!!")
        num2.set("Chega!!!")
        num3.set("Chega!!!")
        num4.set("Chega!!!")
        num5.set("Chega!!!")

gui = Tk()

gui.title("Teste Python+Tkinter")
gui.geometry('300x400')

num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()

btn1 = Button(gui, text="1", command= lambda: insereNumero('1')).pack()
btn2 = Button(gui, text="2", command= lambda: insereNumero('2')).pack()
btn3 = Button(gui, text="3", command= lambda: insereNumero('3')).pack()
btn4 = Button(gui, text="4", command= lambda: insereNumero('4')).pack()
btn5 = Button(gui, text="5", command= lambda: insereNumero('5')).pack()
btn6 = Button(gui, text="6", command= lambda: insereNumero('6')).pack()
btn7 = Button(gui, text="7", command= lambda: insereNumero('7')).pack()
btn8 = Button(gui, text="8", command= lambda: insereNumero('8')).pack()
btn9 = Button(gui, text="9", command= lambda: insereNumero('9')).pack()

label1 = Label(gui, textvariable=num1).pack()
label2 = Label(gui, textvariable=num2).pack()
label3 = Label(gui, textvariable=num3).pack()
label4 = Label(gui, textvariable=num4).pack()
label5 = Label(gui, textvariable=num5).pack()

gui.mainloop()