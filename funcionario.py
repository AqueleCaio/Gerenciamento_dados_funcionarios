from tkinter import *
from datetime import *
from tkinter import messagebox
import pickle, os.path, re

date = datetime.now()
data = date.strftime('%d/%m/%Y\n %H:%M')

class Funcionario():
    def __init__(self, identidade, nome, idade, email, cpf, salario):
        self.identidade = identidade
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf 
        self.salario = salario
        
    @property
    def identidade(self):
        return self.__identidade
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def email(self):
        return self.__email
        
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def salario(self):
        return self.__salario
    
    @identidade.setter
    def identidade(self, id):
        if len(id) <= 0:
            raise ValueError('Número de identidade não indicado')
        
        if len(id) < 4 or len(id) > 4:
            raise ValueError('Número de identidade inválido (deve conter 4 digitos)')
        
        else:
            self.__identidade = id
            
    @nome.setter
    def nome(self, nome):
        if len(nome) <= 0:
            raise ValueError('Nenhum nome foi indicado')
        
        else:
            self.__nome = nome
                
    @email.setter
    def email(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if len(email) <= 0:
            raise ValueError('Email não indicado')
        
        if re.search(regex, email):
            self.__email = email

        else: 
            raise ValueError('Email Inválido')
            
    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) < 11 or len(cpf) > 11:
            raise ValueError('CPF Inválido (O CPF deve conter 11 digitos)')
        
        elif len(cpf) == None:
            raise ValueError('O CPF não foi indicado')
        
        else:
            self.__cpf = cpf
            
    @idade.setter
    def idade(self, idade):
        
        if len(idade) <= 0:
            raise ValueError('Idade não indicada')
        
        if int(idade) < 18: 
            raise ValueError('Idade Insuficiente!')
        
        if int(idade) > 65: 
            raise ValueError('Idade muito grande!')
        
        if int(idade) > 100:
            raise ValueError('Idade Inválida')
        
        else:
            self.__idade = idade     
            
    @salario.setter
    def salario(self, salario):
        if len(salario) <= 0:
            raise ValueError('Nenhum salário foi indicado')  
        
        if int(salario) < 500:
            raise ValueError('Salário inválido') 
        
        else:
            self.__salario = salario


class Aumento(Toplevel):
    def __init__(self, controle, identidade, nome, salario):
        
        Toplevel.__init__(self)
        self.controle = controle
        
        self.title('Alterar salário')
        self.geometry('450x250')
        self.configure(bg='light blue')
        self.resizable(False, False)        

        self.frame_borda = Frame(self, bg='light blue', borderwidth=1, relief='raised')
        self.frame_botao = Frame(self)
        self.frame_novo_salario = Frame(self)
        
        self.identidade = Label(self.frame_borda, text=f'Funcionário {identidade}', bg='light blue')
        self.nome = Label(self.frame_borda, text=f' \ {nome} \ ', bg='light blue')
        self.salario = Label(self.frame_borda, text=f'Salário Atual: R${salario}', bg='light blue')
        self.input_novo_salario = Label(self.frame_novo_salario, text='Inserir Novo Salário ', bg='light blue')
        
        self.novo_salario = Entry(self.frame_novo_salario)
        
        self.botao = Button(self.frame_botao, text='Confirmar Alteração', command=controle.definir_salario) #Passar o def conrirmar alteração
        
        self.frame_borda.pack()
        self.frame_novo_salario.pack()
        self.frame_botao.pack(side='bottom')
        
        self.identidade.pack(side='left', pady=5)
        self.nome.pack(side='left', pady=5)
        self.salario.pack(side='left', pady=5)
        self.input_novo_salario.pack(side='left')
        self.novo_salario.pack()
        self.botao.pack()
        
                
class Cadastra_funcionario(Toplevel):
    def __init__(self, controle):
        
        Toplevel.__init__(self)
        self.controle = controle
        
        self.title('Cadastrar')
        self.geometry('250x250')
        self.configure(bg='light blue')
        self.resizable(False, False)
        
        self.frame_borda = Frame(self, bg='light blue', borderwidth=1, relief='flat')
        self.frame_botao = Frame(self, bg='light blue')
        self.frame_data = Frame(self)

        self.data = Label(self.frame_data, text='{}'.format(data), bg='light blue')
        self.id = Label(self.frame_borda, text='Nº ID:', bg='light blue', foreground='#000')
        self.nome = Label(self.frame_borda, text='Nome:', bg='light blue', foreground='#000')
        self.idade = Label(self.frame_borda, text='Idade:', bg='light blue', foreground='#000')
        self.email = Label(self.frame_borda, text='Email:', bg='light blue', foreground='#000')
        self.cpf = Label(self.frame_borda, text='CPF:', bg='light blue', foreground='#000')
        self.salario = Label(self.frame_borda, text='Salário: ', bg='light blue', foreground='#000')
        
        self.cadastrar = Button(self.frame_botao, text='Cadastrar', command=controle.enter_handler)
        self.salva_funcionarios = Button(self.frame_botao, text='Sair e Salvar', command=controle.salva_dados_funcionarios)
        
        self.input_id = Entry(self.frame_borda, width=10)
        self.input_nome = Entry(self.frame_borda, width=30)
        self.input_idade = Entry(self.frame_borda, width=10)
        self.input_email = Entry(self.frame_borda, width=30)
        self.input_cpf = Entry(self.frame_borda, width=30)
        self.input_salario = Entry(self.frame_borda, width=10)

        self.frame_data.pack(side='top', pady=5)
        self.frame_borda.pack(anchor=CENTER)
        self.frame_botao.pack(side='bottom', pady=5)
        
        self.data.pack()
        self.id.grid(column=0, row=0, sticky=W, pady=2)
        self.nome.grid(column=0, row=1, sticky=W, pady=2)
        self.idade.grid(column=0, row=2, sticky=W, pady=2)
        self.email.grid(column=0, row=3, sticky=W, pady=2) 
        self.cpf.grid(column=0, row=4, sticky=W, pady=2) 
        self.salario.grid(column=0, row=5, sticky=W, pady=2)
        
        self.cadastrar.grid(column=0, row=6, sticky=W, pady=2, padx=2) 
        self.salva_funcionarios.grid(column=1, row=6, sticky=W, pady=2, padx=2)
        
        self.input_id.grid(column=1, row=0, sticky=W, pady=2) 
        self.input_nome.grid(column=1, row=1, sticky=W, pady=2) 
        self.input_idade.grid(column=1, row=2, sticky=W, pady=2)  
        self.input_email.grid(column=1, row=3, sticky=W, pady=2) 
        self.input_cpf.grid(column=1, row=4, sticky=W, pady=2) 
        self.input_salario.grid(column=1, row=5, sticky=W, pady=2) 

    def mostra_janela(self, titulo, menssagem):
        messagebox.showinfo(titulo, menssagem)


class Consulta_funcionario(Toplevel):
    def __init__(self, controle, lista_funcionarios):
        
        Toplevel.__init__(self)
        self.controle = controle
        
        self.title('Consultar')
        self.geometry('250x250')
        self.configure(bg='light blue')
        self.resizable(False, False)
        
        self.frame_listbox = Frame(self, bg='light blue')
        self.frame_botao = Frame(self, bg='light blue')
        
        self.nome = Label(self.frame_listbox, text='Funcionários:', bg='light blue')
        
        self.alterar_salario = Button(self.frame_botao, text='Alterar Salário', command=controle.gerir_salario) #abre a tela para alterar o salario do funcionario
        
        self.listbox = Listbox(self.frame_listbox, width=20, height=10)
        
        self.listbox.bind('<Double-1>', controle.mostra_funcionario)#Passar um metodo double click
        
        for funcionarios in lista_funcionarios:
            self.listbox.insert(0, funcionarios)  
            
        self.frame_listbox.pack()
        self.frame_botao.pack(side='bottom')
                
        self.listbox.pack(side='bottom')
        
        self.alterar_salario.pack(side='right', padx=5, pady=12)
        
        self.nome.pack(side='top')
        
        
class Controle_funcionario():
    def __init__(self):
                
        if not os.path.isfile('funcionarios.pickle'):
            self.lista_funcionarios = []

        else:
            with open ('funcionarios.pickle', 'rb') as file:
                self.lista_funcionarios = pickle.load(file)  
                
                
    def salva_dados_funcionarios(self):
        if len(self.lista_funcionarios) != 0:
            with open ('funcionarios.pickle', 'wb') as file:
                pickle.dump(self.lista_funcionarios, file)
                
                self.cadastro.withdraw()
                
    def insere_funcionario(self):
        self.cadastro = Cadastra_funcionario(self)
        
    def consulta_funcionario(self):
        lista_dados_funcionario = self.get_id_funcionarios()
        self.consulta = Consulta_funcionario(self, lista_dados_funcionario)
        
    #Abre a tela para gerenciar o salario do funcionário
    def gerir_salario(self): #passar nome, identidade e salario para a classe Aumento
        identidade = self.consulta.listbox.get(ACTIVE)
        
        for funcionario in self.lista_funcionarios:
            if identidade[1] == funcionario.identidade:
                identidade = funcionario.identidade
                nome = funcionario.nome
                salario = funcionario.salario
        
        self.aumento = Aumento(self, identidade, nome, salario)
        
    def definir_salario(self): #confirmação da alteração de salario
        novo_salario = self.aumento.novo_salario.get()
        
        try:
            if len(novo_salario) <= 0:
                raise ValueError('Nenhum salário foi indicado')
        
            else:
                for funcionario in self.lista_funcionarios:
                    if funcionario.identidade == self.aumento.identidade:
                        funcionario.salario = novo_salario
                
                self.cadastro.mostra_janela('Sucesso', 'Salário alterado com sucesso')
                
                self.limpa_texto()

        except ValueError as erro:
            self.cadastro.mostra_janela('Erro', erro)
        
    def enter_handler(self):
        identidade = self.cadastro.input_id.get()
        nome = self.cadastro.input_nome.get()
        idade = self.cadastro.input_idade.get()
        email = self.cadastro.input_email.get()
        cpf = self.cadastro.input_cpf.get()
        salario = self.cadastro.input_salario.get()

        try:
            for funcionario in self.lista_funcionarios:
                if identidade in funcionario.identidade and len(identidade) > 1:
                    raise ValueError(f'A identidade {identidade} já consta no registro')
                
                elif identidade in funcionario.identidade and len(identidade) == 0:
                    raise ValueError(f'O número de identidade {identidade} não foi indicado')
                
                #__________________________________________________#
                
                elif nome in funcionario.nome and len(nome) > 1:
                    raise ValueError('Este nome já consta no registro')
                
                elif nome in funcionario.nome and len(nome) == 0:
                    raise ValueError('O nome não foi indicado')
                
                #__________________________________________________#

                elif email in funcionario.email and len(email) > 1:
                    raise ValueError('Este email já consta no registro')
                
                elif email in funcionario.email and len(email) == 0:
                    raise ValueError('O email não foi indicado')
                
                #__________________________________________________#

                elif cpf in funcionario.cpf and len(cpf) > 1: 
                    raise ValueError('Este CPF já consta no registro')
                
                elif cpf in funcionario.cpf and len(cpf) == 0:
                    raise ValueError('O CPF não foi indicado')
                
            else: 
                self.lista_funcionarios.append(Funcionario(identidade, nome, idade, email, cpf, salario))

                self.cadastro.mostra_janela('Sucesso', 'Funcionário Cadastrado com Sucesso')

                self.limpa_texto()   
                
        except ValueError as erro:
            self.cadastro.mostra_janela('Erro', erro)
            
    def get_id_funcionarios(self):
        self.lista_dados_funcionario = []
        
        for funcionario in self.lista_funcionarios:
            identidade = 'Nº:', funcionario.identidade
            
            self.lista_dados_funcionario.append(identidade)
            
        return self.lista_dados_funcionario

    def mostra_funcionario(self, event):
        funcionario = self.consulta.listbox.get(ACTIVE)
        
        for info in self.lista_funcionarios:
            if funcionario[1] == info.identidade:
                info_funcionarios = 'Funcionário {}\n\n'.format(info.identidade)
                info_funcionarios += 'Nome: {}\n\n'.format(info.nome)
                info_funcionarios += 'Idade: {}\n\n'.format(info.idade)
                info_funcionarios += 'Email: {}\n\n'.format(info.email)
                info_funcionarios += 'CPF: {}\n\n'.format(info.cpf)
                info_funcionarios += 'Salário: R${}'.format(info.salario)
        messagebox.showinfo('Funcionário', info_funcionarios)
    
    def limpa_texto(self):
        self.cadastro.input_id.delete(0, END)
        self.cadastro.input_nome.delete(0, END)
        self.cadastro.input_idade.delete(0, END)
        self.cadastro.input_email.delete(0, END)
        self.cadastro.input_cpf.delete(0, END)  
        self.cadastro.input_salario.delete(0, END)
        self.aumento.novo_salario.delete(0, END)
        