from tkinter import *

class Calculadora:
    
    def __init__(self):
        self.root = Tk()
        self.window()
        self.frames()
        
        self.root.mainloop()
    
    #Método para estilizar a janela
    def window(self):
        self.root.geometry('400x550+0+120')
        self.root.resizable(False, False)
        self.root.title('Calculadora 0.1')
    
    #Método para criação dos frames
    def frames(self):
        #No frame01 está condido os botões
        frame01 = Frame(self.root, bg='red', width=400, height=450)
        frame01.grid(row=1)
        frame02 = Frame(self.root, bg='blue', width=400, height=100)
        frame02.grid(row=0)
Calculadora()