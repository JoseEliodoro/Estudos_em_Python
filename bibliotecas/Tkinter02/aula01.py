from re import T
from tkinter import *
from tkinter import ttk

root = Tk()

class Funcs:
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

class Application(Funcs):
    
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        
        root.mainloop()
        
    def tela(self):
        self.root.title('Cadastro de clientes')
        self.root.configure(background='#4682B4') #Coloca cor a janela
        self.root.geometry('700x500') #Define um tamanho original da janela
        self.root.resizable(True, True) #Define se posso aumentar a janela ou não
        self.root.maxsize(width=900, height=700) #Define um tamanho máximo de janela
        self.root.minsize(width=500, height=300) #Define um tamanho mínimo de janela
        
    def frames_da_tela(self):
        #Frame de cadastro de usuários
        self.frame_1 = Frame(self.root, bd= 4, bg='#dfe3ee', 
                             highlightbackground='#759', highlightthickness=3) 
        """ 
        Frames server para dividir a tela em blocos diferentes,
        eles são usados para adicionarmos widgets dentro deles, com 
        intuito de melhorar a manipulação do posicionamento desses elementos
         
        Existem três formas de posicionar elementos numa aplicação do tkinter, são elas
        place, pack e grid.
        pack = menor liberdade de pocisionamento, entretando maior facilidade de manipulação
        grid = transforma em planilhas, posicionamento através de linhas e colunas
        place = abordagem através do x, y, possui posição relativa o que ajuda na adaptabilidade
        """
        self.frame_1.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.46) 
        #relx e rely aceita valores de 0 a 1 sendo (0,0) o quanto esquerdo superior da janela
        #relwidth e relheight aceita valores de 0 a 1 sendo valores referente ao tamanho total da janela
        #Frame de resultado de dados
        self.frame_2 = Frame(self.root, bd= 4, bg='#dfe3ee', 
                            highlightbackground='#759', highlightthickness=3) 
        self.frame_2.place(relx= 0.02,rely= 0.5, relwidth= 0.96, relheight= 0.46) 

    def widgets_frame1(self):
        #Criação do botão de limpar
        self.btn_limpar = Button(self.frame_1, text= 'Limpar', bd=2, 
                                 bg='#187db2',fg='#fff', font='verdana 8 bold', command=self.limpa_tela)
        self.btn_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        
        #Criação do botão de Busca
        self.btn_buscar = Button(self.frame_1, text= 'Buscar', bd=2, 
                                 bg='#187db2',fg='#fff', font='verdana 8 bold')
        self.btn_buscar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        
        #Criação do botão de novo cadastro
        self.btn_novo = Button(self.frame_1, text= 'Novo', bd=2, 
                                 bg='#187db2',fg='#fff', font='verdana 8 bold')
        self.btn_novo.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        
        #Criação do botão de Alterar
        self.btn_alterar = Button(self.frame_1, text= 'Alterar', bd=2, 
                                 bg='#187db2',fg='#fff', font='verdana 8 bold')
        self.btn_alterar.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        
        #Criação do botão de apagar
        self.btn_apagar = Button(self.frame_1, text= 'Apagar', bd=2, 
                                 bg='#187db2',fg='#fff', font='verdana 8 bold')
        self.btn_apagar.place(relx= 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        
        #Criação da label e entrada do dado de código
        lb_codigo = Label(self.frame_1, text= 'Código', bg='#dfe3ee', fg= '#187db2')
        lb_codigo.place(relx= 0.05, rely= 0.05)
        
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.07)
        
        #Criação da label e entrada do dado de nome
        lb_nome = Label(self.frame_1, text= 'Nome', bg='#dfe3ee', fg= '#187db2')
        lb_nome.place(relx= 0.05, rely= 0.35)
        
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.05, rely= 0.45, relwidth= 0.8)
        
        #Criação da label e entrada do dado de telefone
        lb_fone = Label(self.frame_1, text= 'Telefone', bg='#dfe3ee', fg= '#187db2')
        lb_fone.place(relx= 0.05, rely= 0.6)
        
        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx= 0.05, rely= 0.7, relwidth= 0.38)
        
        #Criação da label e entrada do dado de cidade
        lb_cidade = Label(self.frame_1, text= 'Cidade', bg='#dfe3ee', fg= '#187db2')
        lb_cidade.place(relx= 0.47, rely= 0.6)
        
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx= 0.47, rely= 0.7, relwidth= 0.38)
        
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, columns= ('col1', 'col2', 'col3', 'col4'))
        """ 
        Intância do ttk para geração de listas, é preciso identificar através do columns,  
        quantas colunas terá a lista.
        
        O método .heading() serve para nomear as colunas
        """
        self.listaCli.heading("#0",text="")
        self.listaCli.heading("#1",text= "Código")
        self.listaCli.heading("#2",text= "Nome")
        self.listaCli.heading("#3",text= "Telefone")
        self.listaCli.heading("#4",text= "Cidade")
        
        #especificando o tamanho das colunas
        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)
        
        self.listaCli.place(relx= 0.01, rely= 0.1, relwidth= 0.95, relheight= 0.85)
        
        #Criando barra de rolagem para lista
        self.scrollLista = Scrollbar(self.frame_2, orient= 'vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set) #Unindo a scrollbar com a lista
        self.scrollLista.place(relx= 0.96, rely= 0.1, relwidth= 0.025, relheight= 0.85)


        
Application()