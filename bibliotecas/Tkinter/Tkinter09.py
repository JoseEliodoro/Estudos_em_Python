from tkinter import *

window = Tk()
window.title('lista')
window.geometry('300x200')


spin = Spinbox(window, from_=0, to=100, width=5)
#Intância de classe Spinbox para fazer uma lista de números
spin.pack()

spin2 = Spinbox(window, values=(5, 15, 8), width=5)
spin2.pack()


def numero():
    lb['text'] = 'Número selecionado é: '+ spin.get()
    #Pegando o valor do spin

def definir():
    var = IntVar()
    var.set(15)
    spin['textvariable'] = var
    #definindo valor para o spin1
    
btn = Button(window, text='Clique Aqui', command=numero)
btn.pack()
btn2 = Button(window, text='difinir spin1 como 15', command=definir)
btn2.pack()

lb = Label(window, text='Número selecionado')
lb.pack()


window.mainloop()