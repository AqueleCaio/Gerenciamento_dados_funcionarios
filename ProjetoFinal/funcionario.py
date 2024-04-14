import tkinter as tk
from tkinter import messagebox, simpledialog
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


class Dados(tk.Toplevel): # Classe da tela para alterar os dados do funcionário
    def __init__(self, controle, identidade, nome, idade, email, cpf, salario):
        
        tk.Toplevel.__init__(self)
        self.controle = controle
        
        self.title('Alterar salário')
        self.geometry('350x400')
        self.configure(bg='light blue')
        self.resizable(False, False)        
        
        self.frame_forms_alterar = tk.Frame(self, bg='light blue', borderwidth=1, relief='solid')
        self.frame_forms_alterar.pack(padx=50, pady=50, ipadx=10, ipady=10)

        self.frame_cabeçalho = tk.Frame(self.frame_forms_alterar, bg='light blue')
        self.frame_borda = tk.Frame(self.frame_forms_alterar, bg='light blue')
        self.frame_botao = tk.Frame(self.frame_forms_alterar, bg='light blue')
        
        
        ##__________________________Labels__________________________________##        
        self.data = tk.Label(self.frame_cabeçalho, text=f'{data}', bg='light blue')
        self.titulo = tk.Label(self.frame_cabeçalho, text=f'Atuais dados de {nome}', bg='light blue', foreground='#000')
        self.id = tk.Label(self.frame_borda, text='Nº ID:', bg='light blue', foreground='#000')
        self.nome = tk.Label(self.frame_borda, text='Nome:', bg='light blue', foreground='#000')
        self.idade = tk.Label(self.frame_borda, text='Idade:', bg='light blue', foreground='#000')
        self.email = tk.Label(self.frame_borda, text='Email:', bg='light blue', foreground='#000')
        self.cpf = tk.Label(self.frame_borda, text='CPF:', bg='light blue', foreground='#000')
        self.salario = tk.Label(self.frame_borda, text='Salário: ', bg='light blue', foreground='#000')
        
        
        ##__________________________Entries__________________________________##
        self.input_id = tk.Entry(self.frame_borda, width=10)
        self.input_nome =tk.Entry(self.frame_borda, width=30)
        self.input_idade = tk.Entry(self.frame_borda, width=10)
        self.input_email = tk.Entry(self.frame_borda, width=30)
        self.input_cpf = tk.Entry(self.frame_borda, width=30)
        self.input_salario = tk.Entry(self.frame_borda, width=10)
        
        ##_________________________Inserts__________________________________##
        '''
        Insere os dados do funcionário nos campos de entrada para serem alterados 
        pelo usuário.
        '''
        self.input_id.insert(0, identidade)
        self.input_nome.insert(0, nome)
        self.input_idade.insert(0, idade)
        self.input_email.insert(0, email)
        self.input_cpf.insert(0, cpf)
        self.input_salario.insert(0, salario)
        
        
        ##__________________________Botões__________________________________##
        self.confirmar = tk.Button(self.frame_botao, text='Confirmar Alteração', command=controle.altera_dados)
        
        
        ##__________________________Frames__________________________________##
        self.frame_cabeçalho.pack()
        self.frame_borda.pack()
        self.frame_botao.pack(padx=5, pady=10)
        
        
        ##__________________________Grid dos Labels__________________________________##
        self.data.pack()
        self.titulo.pack(padx=5, pady=4)
        
        self.id.grid(column=0, row=0, sticky=tk.W, pady=5)
        self.nome.grid(column=0, row=1, sticky=tk.W, pady=5)
        self.idade.grid(column=0, row=2, sticky=tk.W, pady=5)
        self.email.grid(column=0, row=3, sticky=tk.W, pady=5) 
        self.cpf.grid(column=0, row=4, sticky=tk.W, pady=5) 
        self.salario.grid(column=0, row=5, sticky=tk.W, pady=5)
        
        ##__________________________Grid dos Buttons__________________________________##
        self.confirmar.grid(column=0, row=6, sticky=tk.W, pady=5, padx=5) 
        
        ##__________________________Grid dos Entries__________________________________##
        self.input_id.grid(column=1, row=0, sticky=tk.W, pady=2) 
        self.input_nome.grid(column=1, row=1, sticky=tk.W, pady=2) 
        self.input_idade.grid(column=1, row=2, sticky=tk.W, pady=2)  
        self.input_email.grid(column=1, row=3, sticky=tk.W, pady=2) 
        self.input_cpf.grid(column=1, row=4, sticky=tk.W, pady=2) 
        self.input_salario.grid(column=1, row=5, sticky=tk.W, pady=2)

              
class Cadastra_funcionario(tk.Toplevel):
    def __init__(self, controle, lista_funcionarios):
        
        tk.Toplevel.__init__(self)
        self.controle = controle
        
        self.title('Cadastrar')
        self.geometry('600x400')
        self.configure(bg='light blue')
        self.resizable(False, False) 
        
        ##__________________________Frames principal da esquerda__________________________________##
        self.frame_forms = tk.Frame(self, bg='light blue', borderwidth=1, relief='solid') 
        self.frame_forms.pack(side='left', padx=20, ipadx=10, ipady=17)
        
        ##__________________________Frames principal da direita__________________________________##
        self.frame_lista = tk.Frame(self, bg='light blue') 
        self.frame_lista.pack(side='right', padx=20, ipadx=10, ipady=10)
                
        ##__________________________Frames__________________________________##
        self.frame_borda = tk.Frame(self.frame_forms, bg='light blue', borderwidth=1, relief='flat')
        self.frame_botao = tk.Frame(self.frame_forms, bg='light blue')
        self.frame_cabeçalho = tk.Frame(self.frame_forms, bg='light blue')
        
        self.frame_listbox = tk.Frame(self.frame_lista, bg='light blue')
        self.frame_cabeçalho_list = tk.Frame(self.frame_lista, bg='light blue')
        self.frame_botao_alterar = tk.Frame(self.frame_lista, bg='light blue')
        
        ##__________________________Labels__________________________________##
        self.data = tk.Label(self.frame_cabeçalho, text=f'{data}', bg='light blue')
        self.titulo = tk.Label(self.frame_cabeçalho, text='Fomulário de Adimissão', bg='light blue', foreground='#000')
        self.titulo_list = tk.Label(self.frame_cabeçalho_list, text='Lista de Funcionários', bg='light blue', foreground='#000')
        self.id = tk.Label(self.frame_borda, text='Nº ID:', bg='light blue', foreground='#000')
        self.nome = tk.Label(self.frame_borda, text='Nome:', bg='light blue', foreground='#000')
        self.idade = tk.Label(self.frame_borda, text='Idade:', bg='light blue', foreground='#000')
        self.email = tk.Label(self.frame_borda, text='Email:', bg='light blue', foreground='#000')
        self.cpf = tk.Label(self.frame_borda, text='CPF:', bg='light blue', foreground='#000')
        self.salario = tk.Label(self.frame_borda, text='Salário: ', bg='light blue', foreground='#000')
        
        
        ##__________________________Configuração de Labels__________________________________##
        self.titulo.config(font=('Arial', 13, 'bold'))
        self.titulo_list.config(font=('Arial', 13, 'bold'))
        
        ##__________________________Buttons__________________________________##
        self.cadastrar = tk.Button(self.frame_botao, text='Cadastrar', command=controle.enter_handler)
        self.deleta = tk.Button(self.frame_botao, text='Deletar', command=controle.deleta_funcionario)
        
        self.botao_alterar = tk.Button(self.frame_listbox, text='Alterar Dados', command=controle.gerir_dados)
        
        ##__________________________Entries__________________________________##
        self.input_id = tk.Entry(self.frame_borda, width=10)
        self.input_nome =tk.Entry(self.frame_borda, width=30)
        self.input_idade = tk.Entry(self.frame_borda, width=10)
        self.input_email = tk.Entry(self.frame_borda, width=30)
        self.input_cpf = tk.Entry(self.frame_borda, width=30)
        self.input_salario = tk.Entry(self.frame_borda, width=10)
        
        ##__________________________Listbox__________________________________##
        self.listbox = tk.Listbox(self.frame_listbox, width=27, height=16)
                    
        self.listbox.bind('<Double-1>', lambda event: controle.on_listbox_select(event, self.listbox))#Passar um metodo double click

        #Loop para carregar a lista de funcionários na listbox assim que a tela abre
        for funcionarios in lista_funcionarios:
            self.listbox.insert(0, funcionarios) 
            
        ##__________________________Pack do Listbox__________________________________##
        self.titulo_list.pack()
        self.listbox.pack()
         
        ##__________________________Packs dos Frames__________________________________##
        self.frame_botao_alterar.pack(side='bottom', pady=5) #Botão de alterar do frame_lista (lado direito)
        self.frame_botao.pack(side='bottom', pady=5) #Botões de cadastrar e deletar do frame_forms (lado esquerdo)
        self.frame_cabeçalho.pack(side='top', pady=5)
        self.frame_borda.pack(anchor=tk.CENTER)
        self.frame_listbox.pack(side='bottom', padx=50)
        self.frame_cabeçalho_list.pack(side='top', pady=5)
        
        ##__________________________Grid dos Labels__________________________________##
        self.data.pack()
        self.titulo.pack()
        
        self.id.grid(column=0, row=0, sticky=tk.W, pady=5)
        self.nome.grid(column=0, row=1, sticky=tk.W, pady=5)
        self.idade.grid(column=0, row=2, sticky=tk.W, pady=5)
        self.email.grid(column=0, row=3, sticky=tk.W, pady=5) 
        self.cpf.grid(column=0, row=4, sticky=tk.W, pady=5) 
        self.salario.grid(column=0, row=5, sticky=tk.W, pady=5)
        
        ##__________________________Grid dos Buttons__________________________________##
        self.cadastrar.grid(column=0, row=6, sticky=tk.W, pady=2, padx=5) 
        self.deleta.grid(column=1, row=6, sticky=tk.W, pady=2, padx=5)
        
        self.botao_alterar.pack(side='bottom', pady=10)
        
        ##__________________________Grid dos Entries__________________________________##
        self.input_id.grid(column=1, row=0, sticky=tk.W, pady=2) 
        self.input_nome.grid(column=1, row=1, sticky=tk.W, pady=2) 
        self.input_idade.grid(column=1, row=2, sticky=tk.W, pady=2)  
        self.input_email.grid(column=1, row=3, sticky=tk.W, pady=2) 
        self.input_cpf.grid(column=1, row=4, sticky=tk.W, pady=2) 
        self.input_salario.grid(column=1, row=5, sticky=tk.W, pady=2)


class Controle_funcionario():
    def __init__(self):
        
        if not os.path.isfile('funcionarios.pickle'):
            self.lista_funcionarios = []

        else:
            with open ('funcionarios.pickle', 'rb') as file:
                self.lista_funcionarios = pickle.load(file)  
                
    def insere_funcionario(self):
        lista_dados_funcionario = self.get_id_funcionarios()
        self.cadastro = Cadastra_funcionario(self, lista_dados_funcionario)
                
    def salva_dados_funcionarios(self):
        if len(self.lista_funcionarios) != 0:
            with open ('funcionarios.pickle', 'wb') as file:
                pickle.dump(self.lista_funcionarios, file)
      
                                         
    def deleta_funcionario(self):
        identidade = self.cadastro.listbox.get(tk.ACTIVE)
        
        for funcionario in self.lista_funcionarios:
            if identidade[1] == funcionario.identidade:
                self.lista_funcionarios.remove(funcionario)
                
                self.salva_dados_funcionarios()
                
                self.mostra_janela('Sucesso', 'Funcionário deletado com sucesso')
                
                #faz o funcionário sair da lista de funcionários
                self.cadastro.listbox.delete(tk.ACTIVE)
     
        
    def gerir_dados(self): #Abre a tela para gerenciar os dados do funcionário
        identidade = self.cadastro.listbox.get(tk.ACTIVE)
        
        for funcionario in self.lista_funcionarios:
            if identidade[1] == funcionario.identidade:
                identidade = funcionario.identidade
                nome = funcionario.nome
                idade = funcionario.idade
                email = funcionario.email
                cpf = funcionario.cpf
                salario = funcionario.salario
        
        self.tela_dados = Dados(self, identidade, nome, idade, email, cpf, salario) #passa nome, identidade e salario para a classe tela_dados
        
        
    def altera_dados(self): #confirmação da alteração dos dados
        identidade = self.tela_dados.input_id.get()
        nome = self.tela_dados.input_nome.get()
        idade = self.tela_dados.input_idade.get()
        email = self.tela_dados.input_email.get()
        cpf = self.tela_dados.input_cpf.get()
        salario = self.tela_dados.input_salario.get()
            
        resposta = messagebox.askyesno('Confirmação', 'Deseja realmente alterar os dados?')    
        try:
            if resposta == True:
                for funcionario in self.lista_funcionarios:
                    if identidade == funcionario.identidade:
                        funcionario.identidade = identidade
                        funcionario.nome = nome
                        funcionario.idade = idade
                        funcionario.email = email
                        funcionario.cpf = cpf
                        funcionario.salario = salario
                
                        self.salva_dados_funcionarios() #Salva as novas alterações feitas no salário do funcionário
                        
                        self.mostra_janela('Sucesso', 'Dado(s) alterado(s) com sucesso!')
                        
                        self.tela_dados.destroy()   
            else:
                pass
            
        except ValueError as erro:
            self.mostra_janela('Erro', erro)
        
    #Método que insere o funcionário na lista de funcionários
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

                identidade = 'Nº:', identidade

                # Atualiza a listbox com o novo funcionário
                self.cadastro.listbox.insert(0, identidade)

                self.mostra_janela('Sucesso', 'Funcionário Cadastrado com Sucesso')
                
                #criar um botão para cadastrar e salvar colocando o metodo salva_dados_funcionarios no enter_handler
                self.salva_dados_funcionarios()
                
                self.limpa_texto()   
                
        except ValueError as erro:
            self.mostra_janela('Erro', erro)
            
    #Método que pega o id do funcionário para inserir na listbox
    def get_id_funcionarios(self):
        self.lista_dados_funcionario = []
        
        for funcionario in self.lista_funcionarios:
            identidade = 'Nº:', funcionario.identidade
            
            self.lista_dados_funcionario.append(identidade)
            
        return self.lista_dados_funcionario

    #Método que mostra as informações do funcionário a partir do id
    def mostra_funcionario(self, id_funcionario):
        for info in self.lista_funcionarios:
            if id_funcionario == info.identidade:
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


    #Método que recebe o evento de duplo click e pega o id do funcionário
    def on_listbox_select(self, event, listbox):
        id_funcionario = listbox.get(tk.ACTIVE)
        self.mostra_funcionario(id_funcionario[1])


    def mostra_janela(self, titulo, menssagem):
        messagebox.showinfo(titulo, menssagem)
    
    
    def limpa_texto(self):
        self.cadastro.input_id.delete(0, tk.END)
        self.cadastro.input_nome.delete(0, tk.END)
        self.cadastro.input_idade.delete(0, tk.END)
        self.cadastro.input_email.delete(0, tk.END)
        self.cadastro.input_cpf.delete(0, tk.END)  
        self.cadastro.input_salario.delete(0, tk.END)
        