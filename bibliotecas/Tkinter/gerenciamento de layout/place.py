#Parametro para a utilização do place
""" 
anchor: Posiciona o objeto dentro do espaço a ele alocado. Valor default NW. Pode ser N, E, S, W, NE, NW, SE, ou SW
bordermode: Tipo de borda, valor default INSIDE. INSIDE indica que as outras opções se referem a parte de dentro do widget pai. (ignorando a borda do pai). OUTSIDE opera de forma contrária.
height: altura do widget
in: Mestre relativo ao qual é realizado o posicionamento do widget
relheight: Sem valor default. Altura como uma fração da altura do widget pai. Varia entre 0.0 e 1.0
relwidth: Sem valor default. Largura como uma fração da largura do widget pai. Varia entre 0.0 e 1.0
relx: Valor default 0. Offset horizontal como uma fração da largura do widget pai. Varia entre 0.0 e 1.0
rely: Valor default 0. Offset vertical como uma fração da altura do widget pai. Varia entre 0.0 e 1.0
width: Largura do widget. Valor default 0
x: Valor default 0- Offset horizontal
y: Valor default 0. Offset vertical 
"""
#utilize o método .place() para ativar ele
""" 
Funções adicionais disponibilizadas pelo Place
place_forget(self): Retira o widget da tela. Não destrói o widget, que pode ser inserido novamente quando desejado.
place_info(self): Retorna informação sobre o posicionamento do widget.
place_slaves(self):Retorna uma lista de todos escravos associados ao widget. 
"""
import tkinter as tk
from tkinter import messagebox

def main(args):
 root = tk.Tk()

 btn= tk.Button(root, text ="Click aqui", command = processaBtn)
 btn.place(bordermode=tk.OUTSIDE, height=100, width=100)

 btn1= tk.Button(root, text ="Ou Click aqui", command = processaBtn1)
 btn1.place(bordermode=tk.OUTSIDE, height=100, width=100,x=100, y=100)

 root.mainloop()

 return 0


def processaBtn():
   messagebox.showinfo( "OLá", "Você pressionou o botão certo!")


def processaBtn1():
   messagebox.showinfo( "Ops!!!", "Você pressionou o botão errado!")

if __name__ == '__main__':
 import sys
 sys.exit(main(sys.argv))
