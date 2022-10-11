from cgi import test
from tkinter import *
from tkinter.ttk import * #Importa uma instenção da biblioteca tkinter

window = Tk()
window.geometry('300x200+200+100')
window.title('Olá Mundo')
def exibirValor():
    label['text'] = 'Valor: ' + combo.get()

combo = Combobox(window, cursor='hand2') #Instância da class 
combo['values'] = (1, 2, 3, 4, 5, 'text') #Define os valores que estarão na lista
combo.current(0) #Parametro que define um valor inicial
combo.pack()

label = Label(window, text='Escolha um valor.', font='impact 20 bold')
label.pack()
btn = Button(window, text='Clique Aqui', command=exibirValor)
btn['cursor'] = 'hand2'
btn.pack()
window.mainloop()