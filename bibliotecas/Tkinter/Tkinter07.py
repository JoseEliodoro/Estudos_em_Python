from tkinter import *
from tkinter import scrolledtext #Importando a biblioteca de texto scrolled


window = Tk()
window.title('bloco de texto')
window.geometry('300x200+200+100')

texto = scrolledtext.ScrolledText(window, width= 20, height= 5)
#Instancia da classe ScrolledText
"""
    Caso não defina o width e height eles vão assumir que
    preencem a tela toda
"""
texto.insert(INSERT, 'TEXTO DE EXEMPLO') #Inserindo texto
texto.pack()

def excluir_texto():
    texto.delete(1.0, END) #Exclui o conteúdo do texto
    
    
btn = Button(window, text='Limpar', command=excluir_texto)
btn.pack()

window.mainloop()