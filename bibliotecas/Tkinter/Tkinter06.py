from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title('Radio Button')
window.geometry('300x200+200+100')

mensagem = Label(window, text='Escolha uma opção', font='impacl 20 bold')
mensagem.pack()

def opcao():
    mensagem['text'] = 'Opção Escolhida: '+ escolha.get()
escolha = StringVar()
escolha.set(1) #Força uma seleção em qualquer valor
radio1 = Radiobutton(window,text='PrimeiraOp', value="1",variable = escolha, command=opcao) #Instância de classe para o radio button
""" No viriable está contida a escolha do valor atribuido ao radio button"""
radio2 = Radiobutton(window,text='SergundaOp', value="2",variable = escolha, command=opcao)
radio3 = Radiobutton(window,text='TerceiraOp', value="3",variable = escolha, command=opcao)
radio1.pack()
radio2.pack()
radio3.pack()




window.mainloop()