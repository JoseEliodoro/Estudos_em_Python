from email import message
from tkinter import *
from tkinter import messagebox #Importando a biblioteca de caixa de menssagem


window = Tk()
window.title('caixa de mensagem')
window.geometry('300x200+200+100')

def mensagem_info(): #Mensagem de informação
    messagebox.showinfo('Titulo da caixa', 'Mensagem na caixa')
    
def mensagem_error(): #Mensagem de erro
    messagebox.showerror('Titulo da caixa', 'Mensagem na caixa')
    
def mensagem_warning(): #Mensagem de aviso
    messagebox.showwarning('Titulo da caixa', 'Mensagem na caixa')

btn_info = Button(window, text='mensagem de informação', width=20, command=mensagem_info)
btn_info.pack()

btn_warning = Button(window, text='mensagem de aviso', width=20, command=mensagem_warning)
btn_warning.pack()

btn_error = Button(window, text='mensagem de erro', width=20, command=mensagem_error)
btn_error.pack()

def message_question(): #Mensagem de pergunta com resposta yes/no
    q = messagebox.askquestion('Titulo da pergunta', 'Conteúdo da pergunda')
    print(q) # retorno de yes ou no
    
btn_question = Button(window, text='mensagem de pergunta', width=20, command=message_question)
btn_question.pack()

def message_questionTrueOrFalse(): #Mensagem de pergunta com resposta True/False
    q = messagebox.askyesno('Titulo da pergunta', 'Conteúdo da pergunda')
    print(q) # retorno de True ou False
    
btn_question2 = Button(window, text='True or False', width=20, command=message_questionTrueOrFalse)
btn_question2.pack()

def message_yes_no_cancel(): #Mensagem de pergunta com resposta True/False/None
    q = messagebox.askyesnocancel('Titulo da pergunta', 'Conteúdo da pergunda')
    print(q) # retorno de True, False ou None 
    
btn_question3 = Button(window, text='sim não cancele', width=20, command=message_yes_no_cancel)
btn_question3.pack()

def message_ok_cancel(): #Mensagem de pergunta com resposta Ok cancelar
    q = messagebox.askokcancel('Titulo da pergunta', 'Conteúdo da pergunda')
    print(q) # retorno de True ou False 
    
btn_question4 = Button(window, text='Ok  cancel', width=20, command=message_ok_cancel)
btn_question4.pack()

window.mainloop()

