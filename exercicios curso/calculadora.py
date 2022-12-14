from tkinter import *
from turtle import st, width
from functools import partial
import os
class Calculadora:
    
    def __init__(self):
        self.root = Tk()
        self.window()
        self.frames()
        self.widgets_frame01()
        self.painel()
        self.lista = [0, 0]
        self.last_operation = ''
        self.equal = False
        self.root.mainloop()
    
    #Método para estilizar a janela
    def window(self):
        self.root.geometry('360x550+0+120')
        self.root.resizable(False, False)
        self.root.title('Calculadora 0.1')
    
    #Método para criação dos frames
    def frames(self):
        #No frame01 está condido os botões
        self.frame01 = Frame(self.root)
        self.frame01.place(relx=0.018, rely=0.19, relwidth=1)
        
        #No frame01 está condido os paineis de informação
        self.frame02 = Frame(self.root, bg='blue', width=400, height=100)
        self.frame02.place(relx=0.018, relwidth=1)
        
    #Método para criar os widgets de botão
    def widgets_frame01(self):
        
        self.buttons = list()
        contx = 3
        conty = 1
        #Cria uma lista de botões de 1 a 9
        for button in range(9, 0, -1):
            
            btn = Button(self.frame01, text= str(button), font='Arial 9 bold', bd=0.5)
            btn.grid(column = contx, row=conty, pady= 1,  padx= 1)
            
            contx -= 1
            if(contx == 0):
                contx = 3
                conty += 1
                
            self.buttons19(btn)
            self.buttons.append(btn)
            
        self.btn_mult = Button(self.frame01, text= '*', font='Arial 9 bold', bd=0.5, cursor='hand2')
        self.btn_sum = Button(self.frame01, text= '+', font='Arial 9 bold', bd=0.5, cursor='hand2')
        self.btn_sub = Button(self.frame01, text= '-', font='Arial 9 bold', bd=0.5, cursor='hand2')
        self.btn_divi = Button(self.frame01, text= '/', font='Arial 9 bold', bd=0.5, cursor='hand2')
        self.btn0 = Button(self.frame01, text= '0', font='Arial 9 bold', bd=0.5, cursor='hand2')
        self.btn_enter = Button(self.frame01, text= '=', font='Arial 9 bold', bd=0.5, cursor='hand2')
        self.btn_ce = Button(self.frame01, text= 'C', font='Arial 9 bold', bd=0.5, cursor='hand2')
        self.btn_pont = Button(self.frame01, text='.', font='Arial 9 bold', bd=0.5, cursor='hand2')
            
    
        self.btn_ce.grid(column= 1, row=0, pady= 1,  padx= 1)
        self.btn_divi.grid(column= 2, row=0, pady= 1,  padx= 1)
        self.btn_mult.grid(column= 3, row=0, pady= 1,  padx= 1)
        self.btn_sub.grid(column= 4, row=0, pady= 1,  padx= 1)
        
        self.buttons19(self.btn_ce)
        self.buttons19(self.btn_divi)
        self.buttons19(self.btn_mult)
        self.buttons19(self.btn_sub)
        
        
        self.btn_sum.grid(column= 4, row=1, rowspan=2, pady= 1,  padx= 1)
        self.btn_enter.grid(column= 4, row=3, rowspan=2, pady= 1,  padx= 1)
        
        self.btn_sum['command'] = partial(self.function_buttons, self.btn_sum['text'])
        self.btn_enter['command'] = partial(self.function_buttons, self.btn_enter['text'])
        
        self.btn_enter['width'] = 11
        self.btn_enter['height'] = 11
        self.btn_sum['width'] = 11
        self.btn_sum['height'] = 11
        
        self.btn0.grid(column= 1, row=4, columnspan=2, pady= 1,  padx= 1)
        self.btn_pont.grid(column= 3, row=4, pady= 1,  padx= 1)
        
        self.buttons19(self.btn_pont)
        
        self.btn0['width'] = 23
        self.btn0['height'] = 5
        self.btn0['command'] = partial(self.function_buttons, self.btn0['text'])
    
    #Método para mostra o painel
    def painel(self):
        self.text = StringVar()
        self.text.set('0')
        self.result = Entry(self.frame02, text= self.text, font='Arial 12 bold', justify=RIGHT)
        self.result['state'] ='disable'
        self.result.place(relx= 0.018, rely= 0.6, relwidth=0.95, relheight=0.3)
           
    #Funçõe dos buttons
    def function_buttons(self, a):
        #Cria lista de números em string
        numbers = [str(x) for x  in range(0, 10)]
        var = self.result.get()
        if(self.equal and a in numbers): #bloco para zerar a mémoria caso eu tente fazer um igual e um numero
            
            self.lista = [0, 0]
            self.text.set(0)
            self.equal = False
            
        if((self.lista[1] == 0) and (a in numbers)): 
        #Caso o primeiro digito seja 0 ele vai adicionar diretamento o próximo número
            var = a
            self.lista[1] = float(var)
            
        elif((a in numbers or self.lista[1] == '-')and not(a == '-')):
            var += a  
            self.lista[1] = float(var)
            
        elif(a == '-' and self.lista[1] == 0):
            var = a
            self.lista[1] = var
        elif(a in ['+', '-', '*', '/']):
            
            k = self.lista[1]
            self.lista[1] = 0
            self.last_operation = a
            if(a == '+'):
                if(not(self.equal)):
                    self.lista[0] += k
            elif(a == '-'):
                if(not(self.equal)):
                    self.lista[0] = k + self.lista[0]
                self.lista[1] = '-'
                var = '-'
            elif(a == '*'):
                if(k == 0):
                    k = 1
                elif(self.lista[0] == 0):
                    self.lista[0] = 1
                if(not(self.equal)):
                    self.lista[0] = k * self.lista[0]
            elif(a == '/'):
                if(not(self.equal)):
                    if(self.lista[0] == 0):
                        self.lista[0] = k    
                    else:
                        self.lista[0] = self.lista[0] / k
            self.equal = False        
            

        elif(a == '='):
            self.equal = True
            if(self.last_operation == '+'):
                var = self.lista[0] + self.lista[1]
                self.lista[0] = var
            elif(self.last_operation == '-'):
                var = self.lista[0] + self.lista[1]
                self.lista[0] = var
            elif(self.last_operation == '*'):
                var = self.lista[0] * self.lista[1]
                self.lista[0] = var
            elif(self.last_operation == '/'):
                var = self.lista[0] / self.lista[1]
                self.lista[0] = var
                
        os.system('cls')
        print('self.lista:', self.lista,'\nself.last_operation:',self.last_operation,'\nvar:',var,'\nequal:',self.equal)
        self.text.set(var)
    
    #Método para add estilo nos botões
    def buttons19(self, button):
        button['width'] = 11
        button['height'] = 5
        button['cursor'] = 'hand2'
        button['command'] = partial(self.function_buttons, button['text'])
        
Calculadora()