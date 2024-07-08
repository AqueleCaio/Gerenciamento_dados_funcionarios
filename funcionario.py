import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import pickle, os.path, re
from email_validator import validate_email
import cargo as cargo

date = datetime.now()
data = date.strftime('%d/%m/%Y\n %H:%M')

class Funcionario():
    def __init__(self, identidade, nome, dataNasc, email, cpf, cargo, data_adimissão):
        self.identidade = identidade
        self.nome = nome
        self.dataNasc = dataNasc
        self.email = email
        self.cpf = cpf 
        self.cargo = cargo
        self.__data_adimissão = data_adimissão
        
    @property
    def identidade(self):
        return self.__identidade
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def dataNasc(self):
        return self.__dataNasc
    
    @property
    def email(self):
        return self.__email
        
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def cargo(self):
        return self.__cargo
    
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
            
            
    @dataNasc.setter
    def dataNasc(self, dataNasc):
        # Verifica se a data está no formato dd/mm/aaaa
        if not isinstance(dataNasc, str):
            raise TypeError('Data de nascimento deve ser uma string no formato: dd/mm/aaaa')
        
        if re.match(r'\d{2}/\d{2}/\d{4}', dataNasc) is None:
            raise ValueError('Data de nascimento deve ter o formato: dd/mm/aaaa')
        
        else:
            self.__dataNasc = dataNasc
         
                
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
  
        else:
            self.__cpf = cpf
            
    @cargo.setter
    def cargo(self, cargo):
        #se tiver vazio retorna erro
        if cargo == '':
            raise ValueError('Cargo não informado')
        
        else:
            self.__cargo = cargo
        
             

class Dados(tk.Toplevel): # Classe da tela para alterar os dados do funcionário
    def __init__(self, controle, identidade, nome, dataNasc, email, cpf, lista_cargos):
        
        tk.Toplevel.__init__(self)
        self.controle = controle
        
        self.title('Alterar salário')
        self.geometry('400x400')
        self.configure(bg='light blue')
        self.resizable(False, False)        
        
        self.frame_forms_alterar = tk.Frame(self, bg='light blue', borderwidth=1, relief='solid')
        self.frame_forms_alterar.pack(padx=50, pady=50, ipadx=10, ipady=17)

        self.frame_cabeçalho = tk.Frame(self.frame_forms_alterar, bg='light blue')
        self.frame_borda = tk.Frame(self.frame_forms_alterar, bg='light blue')
        self.frame_botao = tk.Frame(self.frame_forms_alterar, bg='light blue')
        
        
        ##__________________________Labels__________________________________##        
        self.data = tk.Label(self.frame_cabeçalho, text=f'{data}', bg='light blue')
        self.titulo = tk.Label(self.frame_cabeçalho, text=f'Atuais dados de {nome}', bg='light blue', foreground='#000')
        self.id = tk.Label(self.frame_borda, text='Nº ID:', bg='light blue', foreground='#000')
        self.nome = tk.Label(self.frame_borda, text='Nome:', bg='light blue', foreground='#000')
        self.dataNasc = tk.Label(self.frame_borda, text='Data Nasc.:', bg='light blue', foreground='#000')
        self.email = tk.Label(self.frame_borda, text='Email:', bg='light blue', foreground='#000')
        self.cpf = tk.Label(self.frame_borda, text='CPF:', bg='light blue', foreground='#000')
        self.cargo = tk.Label(self.frame_borda, text='Cargo:', bg='light blue', foreground='#000') 
        
        ##__________________________Combobox__________________________________##
        self.comboboxCargo = ttk.Combobox(self.frame_borda, values=lista_cargos, width=20, state="readonly")
        
        
        ##__________________________Entries__________________________________##
        self.input_id = tk.Entry(self.frame_borda, width=10)
        self.input_nome = tk.Entry(self.frame_borda, width=30)
        self.input_dataNasc = tk.Entry(self.frame_borda, width=15)
        self.input_email = tk.Entry(self.frame_borda, width=30)
        self.input_cpf = tk.Entry(self.frame_borda, width=30)
        
        
        ##_________________________Inserts__________________________________##
        '''
        Insere os dados do funcionário nos campos de entrada para serem alterados 
        pelo usuário.
        '''
        self.input_id.insert(0, identidade)
        self.input_nome.insert(0, nome)
        self.input_dataNasc.insert(0, dataNasc)
        self.input_email.insert(0, email)
        self.input_cpf.insert(0, cpf)
        
        
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
        self.dataNasc.grid(column=0, row=2, sticky=tk.W, pady=5)
        self.email.grid(column=0, row=3, sticky=tk.W, pady=5) 
        self.cpf.grid(column=0, row=4, sticky=tk.W, pady=5) 
        self.cargo.grid(column=0, row=5, sticky=tk.W, pady=5)
        
        
        ##__________________________Grid dos Buttons__________________________________##
        self.confirmar.grid(column=0, row=6, sticky=tk.W, pady=5, padx=5) 
        
        ##__________________________Grid dos Entries__________________________________##
        self.input_id.grid(column=1, row=0, sticky=tk.W, pady=2) 
        self.input_nome.grid(column=1, row=1, sticky=tk.W, pady=2) 
        self.input_dataNasc.grid(column=1, row=2, sticky=tk.W, pady=2) 
        self.input_email.grid(column=1, row=3, sticky=tk.W, pady=2) 
        self.input_cpf.grid(column=1, row=4, sticky=tk.W, pady=2) 
        
        ##__________________________Grid dos Combobox__________________________________##
        self.comboboxCargo.grid(column=1, row=5, sticky=tk.W, pady=5)

         
class Cadastra_funcionario(tk.Toplevel):
    def __init__(self, controle, lista_funcionarios, lista_cargos): # passar a lista de cargos pelo controle
        
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
                
        ##__________________________Frames codiovantes da esquerda__________________________________##
        self.frame_borda = tk.Frame(self.frame_forms, bg='light blue', borderwidth=1, relief='flat')
        self.frame_botao_esquerda = tk.Frame(self.frame_forms, bg='light blue')
        self.frame_cabeçalho = tk.Frame(self.frame_forms, bg='light blue')
        
        ##__________________________Frames codiovantes da direita__________________________________##
        self.frame_listbox = tk.Frame(self.frame_lista, bg='light blue')
        self.frame_cabeçalho_list = tk.Frame(self.frame_lista, bg='light blue')
        self.frame_botao_direita = tk.Frame(self.frame_lista, bg='light blue')
        
        ##__________________________Labels__________________________________##
        self.data = tk.Label(self.frame_cabeçalho, text=f'{data}', bg='light blue')
        self.titulo = tk.Label(self.frame_cabeçalho, text='Fomulário de Adimissão', bg='light blue', foreground='#000')
        self.titulo_list = tk.Label(self.frame_cabeçalho_list, text='Lista de Funcionários', bg='light blue', foreground='#000')
        self.id = tk.Label(self.frame_borda, text='Nº ID:', bg='light blue', foreground='#000')
        self.nome = tk.Label(self.frame_borda, text='Nome:', bg='light blue', foreground='#000')
        self.dataNasc = tk.Label(self.frame_borda, text='Data Nasc.:', bg='light blue', foreground='#000')
        self.email = tk.Label(self.frame_borda, text='Email:', bg='light blue', foreground='#000')
        self.cpf = tk.Label(self.frame_borda, text='CPF:', bg='light blue', foreground='#000')
        self.cargo = tk.Label(self.frame_borda, text='Cargo:', bg='light blue', foreground='#000') 
        
        ##__________________________Combobox__________________________________##
        self.comboboxCargo = ttk.Combobox(self.frame_borda, values=lista_cargos, width=20, state="readonly")
        
        
        ##__________________________Configuração de Labels__________________________________##
        self.titulo.config(font=('Arial', 13, 'bold'))
        self.titulo_list.config(font=('Arial', 13, 'bold'))
        
        ##__________________________Buttons__________________________________##
        self.cadastrar = tk.Button(self.frame_botao_esquerda, text='Cadastrar', command=controle.enter_handler)
        
        self.deleta = tk.Button(self.frame_botao_direita, text='Deletar', command=controle.deleta_funcionario)
        self.botao_alterar = tk.Button(self.frame_botao_direita, text='Alterar Dados', command=controle.gerir_dados)
        
        ##__________________________Entries__________________________________##
        self.input_id = tk.Entry(self.frame_borda, width=10)
        self.input_nome = tk.Entry(self.frame_borda, width=30)
        self.input_dataNasc = tk.Entry(self.frame_borda, width=15)
        self.input_email = tk.Entry(self.frame_borda, width=30)
        self.input_cpf = tk.Entry(self.frame_borda, width=30)
        
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
        self.frame_botao_direita.pack(side='bottom', pady=5) #Botão de alterar do frame_lista (lado direito)
        self.frame_botao_esquerda.pack(side='bottom', pady=5) #Botões de cadastrar e deletar do frame_forms (lado esquerdo)
        self.frame_cabeçalho.pack(side='top', pady=5)
        self.frame_borda.pack(anchor=tk.CENTER)
        self.frame_listbox.pack(side='bottom', padx=50)
        self.frame_cabeçalho_list.pack(side='top', pady=5)
        
        ##__________________________Grid dos Labels__________________________________##
        self.data.pack()
        self.titulo.pack()
        
        self.id.grid(column=0, row=0, sticky=tk.W, pady=5)
        self.nome.grid(column=0, row=1, sticky=tk.W, pady=5)
        self.dataNasc.grid(column=0, row=2, sticky=tk.W, pady=5)
        self.email.grid(column=0, row=3, sticky=tk.W, pady=5) 
        self.cpf.grid(column=0, row=4, sticky=tk.W, pady=5) 
        self.cargo.grid(column=0, row=5, sticky=tk.W, pady=5)
        
        ##__________________________Grid dos Buttons__________________________________##
        self.cadastrar.grid(column=0, row=6, sticky=tk.W, pady=5, ipadx=5) 
        
        self.deleta.pack(side='right', pady=10, padx=10)
        self.botao_alterar.pack(side='left', pady=10, padx=10)

        
        ##__________________________Grid dos Entries__________________________________##
        self.input_id.grid(column=1, row=0, sticky=tk.W, pady=2) 
        self.input_nome.grid(column=1, row=1, sticky=tk.W, pady=2) 
        self.input_dataNasc.grid(column=1, row=2, sticky=tk.W, pady=2) 
        self.input_email.grid(column=1, row=3, sticky=tk.W, pady=2) 
        self.input_cpf.grid(column=1, row=4, sticky=tk.W, pady=2) 
        
        ##__________________________Grid dos Combobox__________________________________##
        self.comboboxCargo.grid(column=1, row=5, sticky=tk.W, pady=5)


class Controle_funcionario():
    def __init__(self):
        try:
            if not os.path.isfile('funcionarios.pickle'):
                self.lista_funcionarios = []
            else:
                with open ('funcionarios.pickle', 'rb') as file:
                    self.lista_funcionarios = pickle.load(file)
        except PermissionError:
            print("Erro de permissão ao tentar abrir o arquivo 'funcionarios.pickle'. Por favor, verifique as permissões do arquivo.")
                
                
    def salva_dados_funcionarios(self):
        if len(self.lista_funcionarios) != 0:
            with open ('funcionarios.pickle', 'wb') as file:
                pickle.dump(self.lista_funcionarios, file)
                
                
    def get_cargos_from_file(self):
        if os.path.isfile('cargos.pickle'):
            with open('cargos.pickle', 'rb') as file:
                return pickle.load(file)
        return []
    
    
    def get_nomeCargo(self):
        self.lista_nomeCargo = []
        
        for cargo in self.get_cargos_from_file():
            self.lista_nomeCargo.append(cargo.nome)
        
        return self.lista_nomeCargo
      
                                         
    def insere_funcionario(self):
        lista_dados_funcionario = self.get_id_funcionarios()
        lista_nomes_cargos = self.get_nomeCargo()
        self.cadastro = Cadastra_funcionario(self, lista_dados_funcionario, lista_nomes_cargos)
        
        
    def deleta_funcionario(self):
        identidade = self.cadastro.listbox.get(tk.ACTIVE)
        
        if identidade:  # Verifica se um funcionário está selecionado
            resposta = messagebox.askyesno("Confirmar Exclusão", "Você realmente deseja deletar este funcionário?")
            
            if resposta:  # resposta já é um booleano
                for funcionario in self.lista_funcionarios:
                    if identidade[1] == funcionario.identidade:
                        
                        self.lista_funcionarios.remove(funcionario)
                        
                        self.salva_dados_funcionarios()
                        
                        self.mostra_janela('Sucesso', 'Funcionário deletado com sucesso')
                        
                        self.cadastro.listbox.delete(tk.ACTIVE)
                        break  # Adicione um break para parar o loop após deletar o funcionário
                    
        
    def gerir_dados(self): #Abre a tela para gerenciar os dados do funcionário
        identidade = self.cadastro.listbox.get(tk.ACTIVE)
        lista_nomes_cargos = self.get_nomeCargo()
        
        
        for funcionario in self.lista_funcionarios:
            if identidade[1] == funcionario.identidade:
                identidade = funcionario.identidade
                nome = funcionario.nome
                dataNasc = funcionario.dataNasc
                email = funcionario.email
                cpf = funcionario.cpf
        
        self.tela_dados = Dados(self, identidade, nome, dataNasc, email, cpf, lista_nomes_cargos) 
        
        
    def altera_dados(self): #confirmação da alteração dos dados
        identidade = self.tela_dados.input_id.get()
        nome = self.tela_dados.input_nome.get()
        dataNasc = self.tela_dados.input_dataNasc.get()
        email = self.tela_dados.input_email.get()
        cpf = self.tela_dados.input_cpf.get()
        cargo = self.tela_dados.comboboxCargo.get()
            
        resposta = messagebox.askyesno('Confirmação', 'Deseja realmente alterar os dados?')    
        try:
            if resposta == True:
                for funcionario in self.lista_funcionarios:
                    if identidade == funcionario.identidade:
                        funcionario.identidade = identidade
                        funcionario.nome = nome
                        funcionario.dataNasc = dataNasc
                        funcionario.email = email
                        funcionario.cpf = cpf
                        funcionario.cargo = cargo
                
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
        dataNasc = self.cadastro.input_dataNasc.get()
        email = self.cadastro.input_email.get()
        cpf = self.cadastro.input_cpf.get()
        cargo = self.cadastro.comboboxCargo.get()
        data_adimissão = date.strftime('%d/%m/%Y' ' - ' '%H:%M')
        
        attributes = ['identidade', 'nome', 'email', 'cpf']
        
        try:
            self.dataNasc = dataNasc

            # Calcula a idade e verifica se é maior de 18 anos e menor que 70
            dataNasc_dt = datetime.strptime(self.dataNasc, '%d/%m/%Y')
            today = datetime.today()
            idade = today.year - dataNasc_dt.year - ((today.month, today.day) < (dataNasc_dt.month, dataNasc_dt.day))
            if idade < 18 or idade > 70:
                raise ValueError('Idade inválida')

            for funcionario in self.lista_funcionarios:
                for attr in attributes:
                    value = getattr(funcionario, attr)
                    input_value = locals()[attr]

                    if input_value in value and len(input_value) > 1:
                        raise ValueError(f'O {attr} {input_value} já consta no registro')
                    elif input_value in value and len(input_value) == 0:
                        raise ValueError(f'O {attr} não foi indicado')

            else: 
                self.lista_funcionarios.append(Funcionario(identidade, nome, dataNasc, email, cpf, cargo, data_adimissão))

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
                
                #Calcula a idade do funcionário a partir da data de nascimento
                idade = datetime.strptime(info.dataNasc, '%d/%m/%Y')
                idade = date.year - idade.year - ((date.month, date.day) < (idade.month, idade.day))
                
                # Formatar o CPF com pontos e traços
                cpf = info.cpf[:3] + '.' + info.cpf[3:6] + '.' + info.cpf[6:9] + '-' + info.cpf[9:]
                
                # Criar a string de informações do funcionário usando uma lista e o método join
                info_funcionarios = '\n\n'.join([
                    f'Funcionário {info.identidade}',
                    f'Nome: {info.nome}',
                    f'Idade: {idade}',
                    f'Email: {info.email}',
                    f'CPF: {cpf}',
                    f'Cargo: {info.cargo}',
                    f'Data de Adimissão: {info.data_adimissão}'
                ])
                
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
        self.cadastro.input_dataNasc.delete(0, tk.END)
        self.cadastro.input_email.delete(0, tk.END)
        self.cadastro.input_cpf.delete(0, tk.END)  
        self.cadastro.comboboxCargo.set("") 
        