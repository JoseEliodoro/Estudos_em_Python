from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk

window = Tk()
window.title('Barra de progresso')
window.geometry('350x200')

style = ttk.Style()
style.theme_use('default')
style.configure(
    "red.Horizontal.TProgressbar",
    background = 'red'
)

barra = Progressbar(
    window, length=200,
    style='red.Horizontal.TProgressbar')
barra['value'] = 70
barra.pack()

barra2 = Progressbar(window, length=200, value= 40)
barra2.pack()




window.mainloop()