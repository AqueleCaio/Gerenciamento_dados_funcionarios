import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pickle, os.path, re
from email_validator import validate_email

date = datetime.now()
data = date.strftime('%d/%m/%Y\n %H:%M')

class Funcionario():
    def __init__(self, identidade, nome, idade, email, cpf, salario, data_adimissão):
        self.identidade = identidade
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf 
        self.salario = salario
        self.__data_adimissão = data_adimissão
        
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
    
    @property
    def data_adimissão(self):
        return self.__data_adimissão
    

    @identidade.setter
    def identidade(self, id):
        if len(id) < 4 or len(id) > 4:
            raise ValueError('Número de identidade inválido (deve conter 4 digitos)')
        
        elif int(id) == False:
            raise ValueError('Identidade inválida')
        
        else:
            self.__identidade = id
            
    @nome.setter
    def nome(self, nome):
        #valida se o nome contem numeros ou caracteres especiais
        if re.search('[0-9]', nome) or re.search('[!@#$%&*()_+=]', nome):
            raise ValueError('Nome inválido')
        
        #valida se o nome contem nome e sobrenome
        elif len(nome.split()) < 2:
            raise ValueError('Deve conter nome e sobrenome')
  
        else:
            self.__nome = nome
                
    @email.setter
    def email(self, email):
        valide_email = validate_email(email)
        dominio = valide_email['email'].split('@')[1].split('.')[0]
        dominios = ['gmail', 'hotmail', 'yahoo', 'outlook']
        
        if validate_email == False or dominio not in dominios:
            raise ValueError('Email inválido')
        
        else:
            self.__email = email
            
    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) < 11 or len(cpf) > 11:
            raise ValueError('CPF deve conter 11 digitos')
        
        elif int(cpf) == False:
            raise ValueError('CPF inválido')
        
        else:
            self.__cpf = cpf
            
    @idade.setter
    def idade(self, idade):
        if len(idade) <= 0:
            raise ValueError('Idade não indicada')
        
        elif int(idade) < 18: 
            raise ValueError('Idade Insuficiente!')
        
        elif int(idade) > 70: 
            raise ValueError('Idade muito grande!')
        
        else:
            self.__idade = idade     
            
    @salario.setter
    def salario(self, salario):
        if int(salario) < 500:
            raise ValueError('Salário inválido') 
        
        else:
            self.__salario = salario


class Aumento(tk.Toplevel):
    def __init__(self, controle, identidade, nome, salario):
        
        tk.Toplevel.__init__(self)
        self.controle = controle
        
        self.title('Alterar salário')
        self.geometry('350x150')
        self.configure(bg='light blue')
        self.resizable(False, False)        

        self.frame_borda = tk.Frame(self, bg='light blue', borderwidth=1, relief='raised')
        self.frame_botao = tk.Frame(self)
        self.frame_novo_salario = tk.Frame(self, bg='light blue')
        
        self.identidade = tk.Label(self.frame_borda, text=f'Funcionário {identidade}', bg='light blue')
        self.nome = tk.Label(self.frame_borda, text=f'{nome}  ', bg='light blue')
        self.salario = tk.Label(self.frame_borda, text=f'Salário Atual: R${salario}', bg='light blue')
        self.input_novo_salario = tk.Label(self.frame_novo_salario, text='Inserir Novo Salário ', bg='light blue')
        
        self.novo_salario = tk.Entry(self.frame_novo_salario)
        
        self.botao = tk.Button(self.frame_botao, text='Confirmar Alteração', command=controle.definir_salario) #Passar o def conrirmar alteração
        
        self.frame_borda.pack()
        self.frame_novo_salario.pack()
        self.frame_botao.pack(side='bottom')
        
        self.identidade.pack(side='left', pady=5)
        self.nome.pack(side='left', pady=5)
        self.salario.pack(side='left', pady=5)
        self.input_novo_salario.pack(side='left')
        self.novo_salario.pack(anchor=tk.CENTER, pady=35, padx=5) #pady e padx para o botão ficar no centro
        self.botao.pack()

#ipad é o espaçamento interno do frame
#pad é o espaçamento externo do frame
                
class Cadastra_funcionario(tk.Toplevel):
    def __init__(self, controle):
        
        tk.Toplevel.__init__(self)
        self.controle = controle
        
        self.title('Cadastrar')
        self.geometry('600x400')
        self.configure(bg='light blue')
        self.resizable(False, False)
        
        self.frame_gigante = tk.Frame(self, bg='light blue', borderwidth=1, relief='solid')
        self.frame_gigante.pack(side='left', ipadx=5, ipady=5, padx=5, pady=5)
                
        ##__________________________Frames__________________________________##
        self.frame_borda = tk.Frame(self.frame_gigante, bg='light blue', borderwidth=1, relief='flat')
        self.frame_botao = tk.Frame(self.frame_gigante, bg='light blue')
        self.frame_cabeçalho = tk.Frame(self.frame_gigante, bg='light blue')

        ##__________________________Labels__________________________________##
        self.data = tk.Label(self.frame_cabeçalho, text=f'{data}', bg='light blue')
        self.titulo = tk.Label(self.frame_cabeçalho, text='Fomulário de Adimissão', bg='light blue', foreground='#000')
        self.id = tk.Label(self.frame_borda, text='Nº ID:', bg='light blue', foreground='#000')
        self.nome = tk.Label(self.frame_borda, text='Nome:', bg='light blue', foreground='#000')
        self.idade = tk.Label(self.frame_borda, text='Idade:', bg='light blue', foreground='#000')
        self.email = tk.Label(self.frame_borda, text='Email:', bg='light blue', foreground='#000')
        self.cpf = tk.Label(self.frame_borda, text='CPF:', bg='light blue', foreground='#000')
        self.salario = tk.Label(self.frame_borda, text='Salário: ', bg='light blue', foreground='#000')
        
        ##__________________________Configuração de Labels__________________________________##
        self.titulo.config(font=('Arial', 13, 'bold'))
        
        ##__________________________Buttons__________________________________##
        self.cadastrar = tk.Button(self.frame_botao, text='Cadastrar', command=controle.enter_handler)
        self.sair = tk.Button(self.frame_botao, text='Sair', command=controle.salva_dados_funcionarios)
        
        ##__________________________Entries__________________________________##
        self.input_id = tk.Entry(self.frame_borda, width=10)
        self.input_nome =tk.Entry(self.frame_borda, width=30)
        self.input_idade = tk.Entry(self.frame_borda, width=10)
        self.input_email = tk.Entry(self.frame_borda, width=30)
        self.input_cpf = tk.Entry(self.frame_borda, width=30)
        self.input_salario = tk.Entry(self.frame_borda, width=10)
        
        ##__________________________Packs dos Frames__________________________________##
        self.frame_botao.pack(side='bottom', pady=5)
        self.frame_cabeçalho.pack(side='top', pady=5)
        self.frame_borda.pack(anchor=tk.CENTER)
        
        ##__________________________Grid dos Labels__________________________________##
        self.data.pack()
        self.titulo.pack()
        self.id.grid(column=0, row=0, sticky=tk.W, pady=2)
        self.nome.grid(column=0, row=1, sticky=tk.W, pady=2)
        self.idade.grid(column=0, row=2, sticky=tk.W, pady=2)
        self.email.grid(column=0, row=3, sticky=tk.W, pady=2) 
        self.cpf.grid(column=0, row=4, sticky=tk.W, pady=2) 
        self.salario.grid(column=0, row=5, sticky=tk.W, pady=2)
        
        ##__________________________Grid dos Buttons__________________________________##
        self.cadastrar.grid(column=0, row=6, sticky=tk.W, pady=2, padx=2) 
        self.sair.grid(column=1, row=6, sticky=tk.W, pady=2, padx=2)
        
        ##__________________________Grid dos Entries__________________________________##
        self.input_id.grid(column=1, row=0, sticky=tk.W, pady=2) 
        self.input_nome.grid(column=1, row=1, sticky=tk.W, pady=2) 
        self.input_idade.grid(column=1, row=2, sticky=tk.W, pady=2)  
        self.input_email.grid(column=1, row=3, sticky=tk.W, pady=2) 
        self.input_cpf.grid(column=1, row=4, sticky=tk.W, pady=2) 
        self.input_salario.grid(column=1, row=5, sticky=tk.W, pady=2)


class Consulta_funcionario(tk.Toplevel):
    def __init__(self, controle, lista_funcionarios):
        
        tk.Toplevel.__init__(self)
        self.controle = controle
        
        self.title('Consultar')
        self.geometry('250x250')
        self.configure(bg='light blue')
        self.resizable(False, False)
        
        self.frame_listbox = tk.Frame(self, bg='light blue')
        self.frame_botao = tk.Frame(self, bg='light blue')
        
        self.nome = tk.Label(self.frame_listbox, text='Funcionários:', bg='light blue')
        
        self.alterar_salario = tk.Button(self.frame_botao, text='Alterar Salário', command=controle.gerir_salario) #abre a tela para alterar o salario do funcionario
        self.deleta = tk.Button(self.frame_botao, text='Deletar', command=controle.deleta_funcionario)
        
        self.listbox = tk.Listbox(self.frame_listbox, width=20, height=10)
        
        self.listbox.bind('<Double-1>', controle.mostra_funcionario)#Passar um metodo double click
        
        for funcionarios in lista_funcionarios:
            self.listbox.insert(0, funcionarios)  
            
        self.frame_listbox.pack()
        self.frame_botao.pack(side='bottom')
                
        self.listbox.pack(side='bottom')
        
        self.alterar_salario.pack(side='right', padx=5, pady=12)
        self.deleta.pack(side='right', padx=5, pady=12)
        
        self.nome.pack(side='top')

class Controle_funcionario():
    def __init__(self):
        
        if not os.path.isfile('funcionarios.pickle'):
            self.lista_funcionarios = []

        else:
            with open ('funcionarios.pickle', 'rb') as file:
                self.lista_funcionarios = pickle.load(file)  
                
    def insere_funcionario(self):
        self.cadastro = Cadastra_funcionario(self)
                
    def salva_dados_funcionarios(self):
        if len(self.lista_funcionarios) != 0:
            with open ('funcionarios.pickle', 'wb') as file:
                pickle.dump(self.lista_funcionarios, file)
                
                self.cadastro.destroy()
                
                                
    def deleta_funcionario(self):
        identidade = self.consulta.listbox.get(tk.ACTIVE)
        
        for funcionario in self.lista_funcionarios:
            if identidade[1] == funcionario.identidade:
                self.lista_funcionarios.remove(funcionario)
                
                self.salva_dados_funcionarios()
                
                self.mostra_janela('Sucesso', 'Funcionário deletado com sucesso')
                
                #faz o funcionário sair da lista de funcionários
                self.consulta.listbox.delete(tk.ACTIVE)
        
    def consulta_funcionario(self):
        lista_dados_funcionario = self.get_id_funcionarios()
        self.consulta = Consulta_funcionario(self, lista_dados_funcionario)
        
    def gerir_salario(self): #Abre a tela para gerenciar o salario do funcionário
        identidade = self.consulta.listbox.get(tk.ACTIVE)
        
        for funcionario in self.lista_funcionarios:
            if identidade[1] == funcionario.identidade:
                identidade = funcionario.identidade
                nome = funcionario.nome
                salario = funcionario.salario
        
        self.aumento = Aumento(self, identidade, nome, salario) #passa nome, identidade e salario para a classe Aumento
        
        
    def definir_salario(self): #confirmação da alteração de salario
        novo_salario = self.aumento.novo_salario.get()
        identidade = self.consulta.listbox.get(tk.ACTIVE)

        try:
            if len(novo_salario) <= 0:
                raise ValueError('Nenhum salário foi indicado')
            
            elif int(novo_salario) < 500:
                raise ValueError('Salário inválido')
        
            else:
                for funcionario in self.lista_funcionarios:
                    if identidade[1] == funcionario.identidade:
                        funcionario.salario = novo_salario  
                
                self.salva_dados_funcionarios() #Salva as novas alterações feitas no salário do funcionário
                
                self.mostra_janela('Sucesso', 'Salário alterado com sucesso')
                
                self.aumento.destroy()

        except ValueError as erro:
            self.mostra_janela('Erro', erro)
        
    def enter_handler(self):
        identidade = self.cadastro.input_id.get()
        nome = self.cadastro.input_nome.get()
        idade = self.cadastro.input_idade.get()
        email = self.cadastro.input_email.get()
        cpf = self.cadastro.input_cpf.get()
        salario = self.cadastro.input_salario.get()
        data_adimissão = date.strftime('%d/%m/%Y' ' - ' '%H:%M')
        
        try:
            for funcionario in self.lista_funcionarios:
                if identidade in funcionario.identidade and len(identidade) > 1:
                    raise ValueError(f'A identidade {identidade} já consta no registro')
                
                elif identidade in funcionario.identidade and len(identidade) == 0:
                    raise ValueError('O número de identidade não foi indicado')
                
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
                
                #__________________________________________________#
                
            else: 
                self.lista_funcionarios.append(Funcionario(identidade, nome, idade, email, cpf, salario, data_adimissão))

                self.mostra_janela('Sucesso', 'Funcionário Cadastrado com Sucesso')
                
                #criar um botão para cadastrar e salvar colocando o metodo salva_dados_funcionarios no enter_handler
                self.salva_dados_funcionarios()
                
                self.limpa_texto()   
                
        except ValueError as erro:
            self.mostra_janela('Erro', erro)
            
    def get_id_funcionarios(self):
        self.lista_dados_funcionario = []
        
        for funcionario in self.lista_funcionarios:
            identidade = 'Nº:', funcionario.identidade
            
            self.lista_dados_funcionario.append(identidade)
            
        return self.lista_dados_funcionario

    def mostra_funcionario(self, event):
        funcionario = self.consulta.listbox.get(tk.ACTIVE)
        
        for info in self.lista_funcionarios:
            if funcionario[1] == info.identidade:
                info_funcionarios = f'Funcionário {info.identidade}\n\n'
                info_funcionarios += f'Nome: {info.nome}\n\n'
                info_funcionarios += f'Idade: {info.idade}\n\n'
                info_funcionarios += f'Email: {info.email}\n\n'
                #faz com que na consulta o cpf apareça com pontos e traços
                cpf = info.cpf[:3] + '.' + info.cpf[3:6] + '.' + info.cpf[6:9] + '-' + info.cpf[9:]
                info_funcionarios += f'CPF: {cpf}\n\n'
                info_funcionarios += f'Salário: R${info.salario}\n\n'
                info_funcionarios += f'Data de Adimissão: {info.data_adimissão}'
        self.mostra_janela('Funcionário', info_funcionarios)
    
    def mostra_janela(self, titulo, menssagem):
        messagebox.showinfo(titulo, menssagem)
    
    def limpa_texto(self):
        self.cadastro.input_id.delete(0, tk.END)
        self.cadastro.input_nome.delete(0, tk.END)
        self.cadastro.input_idade.delete(0, tk.END)
        self.cadastro.input_email.delete(0, tk.END)
        self.cadastro.input_cpf.delete(0, tk.END)  
        self.cadastro.input_salario.delete(0, tk.END)
        