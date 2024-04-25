import tkinter as tk
from tkinter import messagebox
import pickle, os.path

class Cargos:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def salario(self):
        return self.__salario
    
    @nome.setter
    def nome(self, nome):
        if nome == '':
            raise ValueError('Nome não pode ser vazio')
        
        elif not isinstance(nome, str):
            raise ValueError('Nome deve ser uma string')
        
        else:
            self.__nome = nome
            
    @salario.setter
    def salario(self, salario):
        if salario == '':
            raise ValueError('Salário não pode ser vazio')
        
        elif str(salario).isdigit() == False:
            raise ValueError('Salário deve ser um número')
        
        else:
            self.__salario = salario
            

class View_cargos(tk.Toplevel): 
    def __init__(self, controle, lista_cargo): 
        
        tk.Toplevel.__init__(self)
        self.controle = controle
                
        self.title('Cargos')
        self.geometry('350x450')
        self.configure(bg='light blue')
        self.resizable(False, False)

        self.frame = tk.Frame(self, bg='light blue') #frame principal
        self.frame_inputs = tk.Frame(self.frame, bg='light blue')
        
        self.nome = tk.Label(self.frame_inputs, text='Cargo', bg='light blue')
        self.salario = tk.Label(self.frame_inputs, text='Salário', bg='light blue')

        self.input_nome = tk.Entry(self.frame_inputs)
        self.input_salario = tk.Entry(self.frame_inputs)

        self.listbox = tk.Listbox(self.frame, width=27, height=14)

        for cargo in lista_cargo:
            self.listbox.insert(tk.END, cargo)

        self.botao_adiciona = tk.Button(self.frame, text='Adicionar', command=controle.enterHandler)
        self.botao_deleta = tk.Button(self.frame, text='Deletar', command=controle.deleta_cargo)


        self.frame.pack()
        self.frame_inputs.pack()
        
        self.nome.grid(row=0, column=0, sticky='w', pady=5)
        self.salario.grid(row=1, column=0, sticky='w', pady=5)
        
        self.input_nome.grid(row=0, column=1, sticky='w', pady=5)
        self.input_salario.grid(row=1, column=1, sticky='w', pady=5)

        self.listbox.pack(padx=5, pady=5)
        
        self.botao_adiciona.pack(padx=5, pady=5)
        self.botao_deleta.pack(padx=5, pady=5)


class Controle_cargos:
    def __init__(self):
        
        if not os.path.isfile('cargos.pickle'):
            self.lista_cargos = []

        else:
            with open ('cargos.pickle', 'rb') as file:
                self.lista_cargos = pickle.load(file) 
        
    def insere_cargo(self): #abre a tela para inserir os cargos
        lista_cargo = self.get_nome()
        self.cargo = View_cargos(self, lista_cargo)
        
        
    def enterHandler(self):
        nome = self.cargo.input_nome.get()
        salario = self.cargo.input_salario.get()
        
        try:
            self.lista_cargos.append(Cargos(nome, salario))
            
            listbox = self.cargo.listbox
            listbox.insert(tk.END, nome)
            
        except ValueError as erro:
            messagebox.showerror('Erro', erro)
            
    def get_nome(self):
        self.lista_cargo = []
        for cargo in self.lista_cargos:
            self.lista_cargo.append(cargo.nome)
            
        return self.lista_cargo
    
    def deleta_cargo(self):
        self.cargo_sel = self.cargo.listbox.get(tk.ACTIVE)
        
        for cargo in self.lista_cargos:
            if cargo.nome == self.cargo_sel:
                self.lista_cargos.remove(cargo)
                self.cargo.listbox.delete(tk.ACTIVE)
                break
            
    
    