from tkinter import *
from tkinter.ttk import * #Importa uma extenção da biblioteca tkinter

window = Tk()
window.title('Checkbox')
window.geometry('300x200+200+100')
def recuperarEstado():
    if botaoMarcavelStatus.get() == True:
        valor = 'sim'
    else:
        valor = 'não'
    mensagem['text'] = 'valor: '+ valor

mensagem = Label(window, text='Marcado: sim', font='impact 20 bold')
mensagem.pack()    

botaoMarcavelStatus = BooleanVar()
botaoMarcavelStatus.set(False) #Define o status padrão do check_box

check_box = Checkbutton(window, text='Marqui aqui', var=botaoMarcavelStatus)
#Instância de classe para check_box
check_box.pack()



btn = Button(window, text='Clique Aqui', command=recuperarEstado)
btn.pack()


window.mainloop()