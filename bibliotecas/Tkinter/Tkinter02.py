from tkinter import *
from tkinter import font
window = Tk() #instancia a classe tk, que é uma classe de janela 
window.title('Ti fora da caixa') #Coloca um titulo na janela

#Definindo label
lb = Label(window, text='Olá Mundo', fg="green") 
""" 
Instancia um label 
o primeiro paramatro é o nome da janela ao qual ele será inserido
o segundo é a string que aparecerá no label
inserir é diferente de adicionar
"""
lb['text'] = 'Este texto será exibido'
lb['font'] = 'impact 20 bold' #Altera a fonte o tamanho e o estilo do texto
lb.pack() #add o label na janela

#Definindo botão
def clicou():
    lb['text'] = 'clicou no botão'
btn = Button(window, text="Clique Aqui") #instanciando o botão
btn['bg'] = 'black' #bg = background também pode ser add na instancia de classe igual o text=
btn['fg'] = '#fff' #fg = color font 
btn['command'] = clicou #Comando para caso o botão seja clicado. PS não coloque parenteses na função

btn.pack() #Add o btn na janela

window.geometry('800x600') #Método que define um tamanho apra a janela
""" 
O método .geometry()  pode receber 4 valores sendo eles nessa ordem
'alturaXlargura+MargemEsquerda+MargemTopo'
"""
window.mainloop() #Faz com que a janela continue ativa até alguém fechar ela
#Sem esse comando ao iniciar a aplicação ela fecha na mesma hora
