from tkinter import *

window = Tk() #instância da janela
window.geometry('300x200+200+100')
window.title('Titulos Aqui')

def aoclicar():
    mensagem['text'] = 'texto: '+ entrada.get()
    #Método .get() extrai o valor que está no text_box
    
entrada = Entry(window, font='arial 15 bold') #instância de um text_box
entrada['state'] = 'disabled' #Desativa a interação com o usuário
entrada.pack()

mensagem = Label(window, text='Digite alguma coisa', font='impact 20 bold')
mensagem.pack()

botao = Button(window, text='Clique Aqui', command=aoclicar)
#botao['state'] = 'disabled'
botao.pack()


entrada.focus() #O método .focus() já deixa um elemento como foco do usuário
window.mainloop()