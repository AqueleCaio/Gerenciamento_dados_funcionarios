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

         
class CadastraFuncionario(tk.Toplevel):
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
                    
        self.listbox.bind('<Double-1>', lambda event: controle._get_item_selecionado(event, self.listbox))#Passar um metodo double click

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


class ControleFuncionario:
    def __init__(self):
        self.lista_funcionarios = self._carregar_arquivo('funcionarios.pickle', [])

    @staticmethod
    def _carregar_arquivo(nome_arquivo, valor_padrao):
        try:
            if os.path.isfile(nome_arquivo):
                with open(nome_arquivo, 'rb') as file:
                    return pickle.load(file)
        except PermissionError:
            print(f"Erro de permissão ao tentar abrir o arquivo '{nome_arquivo}'.")
        return valor_padrao

    @staticmethod
    def _salvar_arquivo(nome_arquivo, dados):
        if dados:
            with open(nome_arquivo, 'wb') as file:
                pickle.dump(dados, file)

    def salva_dados_funcionarios(self):
        self._salvar_arquivo('funcionarios.pickle', self.lista_funcionarios)

    def get_cargos(self):
        return self._carregar_arquivo('cargos.pickle', [])

    def get_nome_cargos(self):
        return [cargo.nome for cargo in self.get_cargos()]

    def insere_funcionario(self):
        lista_dados_funcionario = self.get_id_funcionarios()
        lista_nomes_cargos = self.get_nome_cargos()
        self.cadastro = CadastraFuncionario(self, lista_dados_funcionario, lista_nomes_cargos)

    def deleta_funcionario(self):
        identidade = self._get_item_selecionado(self.cadastro.listbox)

        if identidade and self._confirma_acao("Confirmar Exclusão", "Você realmente deseja deletar este funcionário?"):
            funcionario = next((f for f in self.lista_funcionarios if f.identidade == identidade), None)
            if funcionario:
                self.lista_funcionarios.remove(funcionario)
                self._atualiza_listbox(self.cadastro.listbox)
                self.salva_dados_funcionarios()
                self.mostra_janela('Sucesso', 'Funcionário deletado com sucesso')

    def gerir_dados(self):
        identidade = self._get_item_selecionado(self.cadastro.listbox)
        funcionario = next((f for f in self.lista_funcionarios if f.identidade == identidade), None)

        if funcionario:
            self.tela_dados = Dados(
                self,
                funcionario.identidade,
                funcionario.nome,
                funcionario.dataNasc,
                funcionario.email,
                funcionario.cpf,
                self.get_nome_cargos()
            )

    def altera_dados(self):
        if self._confirma_acao('Confirmação', 'Deseja realmente alterar os dados?'):
            identidade = self.tela_dados.input_id.get()
            funcionario = next((f for f in self.lista_funcionarios if f.identidade == identidade), None)

            if funcionario:
                self._atualiza_atributos(funcionario, self.tela_dados)
                self.salva_dados_funcionarios()
                self.mostra_janela('Sucesso', 'Dado(s) alterado(s) com sucesso!')
                self.tela_dados.destroy()

    def enter_handler(self):
        try:
            dados = self._coleta_dados_formulario(self.cadastro)
            self._valida_dados(dados)
            self.lista_funcionarios.append(Funcionario(**dados))
            self.salva_dados_funcionarios()
            self._atualiza_listbox(self.cadastro.listbox)
            self.mostra_janela('Sucesso', 'Funcionário cadastrado com sucesso')
        except ValueError as erro:
            self.mostra_janela('Erro', str(erro))

    def get_id_funcionarios(self):
        return [(f'Nº: {f.identidade}', f.identidade) for f in self.lista_funcionarios]

    def _valida_dados(self, dados):
        data_nasc_dt = datetime.strptime(dados['dataNasc'], '%d/%m/%Y')
        hoje = datetime.today()
        idade = hoje.year - data_nasc_dt.year - ((hoje.month, hoje.day) < (data_nasc_dt.month, data_nasc_dt.day))

        if idade < 18 or idade > 70:
            raise ValueError('Idade inválida')
        
        for funcionario in self.lista_funcionarios:
            for attr in ['identidade', 'nome', 'email', 'cpf']:
                if dados[attr] == getattr(funcionario, attr):
                    atributo_duplicado = attr
                    break
            else:
                continue  # Continua para o próximo funcionário se nenhum atributo duplicado for encontrado
            break  # Interrompe o loop principal se um atributo duplicado for encontrado

        if atributo_duplicado:
            raise ValueError(f'Este {atributo_duplicado} já consta no registro')


    def _coleta_dados_formulario(self, formulario):
        return {
            'identidade': formulario.input_id.get(),
            'nome': formulario.input_nome.get(),
            'dataNasc': formulario.input_dataNasc.get(),
            'email': formulario.input_email.get(),
            'cpf': formulario.input_cpf.get(),
            'cargo': formulario.comboboxCargo.get(),
            'data_adimissão': datetime.now().strftime('%d/%m/%Y - %H:%M')
        }

    def _atualiza_listbox(self, listbox):
        listbox.delete(0, tk.END)
        for identidade in self.get_id_funcionarios():
            listbox.insert(tk.END, identidade)

    def _atualiza_atributos(self, funcionario, tela):
        funcionario.identidade = tela.input_id.get()
        funcionario.nome = tela.input_nome.get()
        funcionario.dataNasc = tela.input_dataNasc.get()
        funcionario.email = tela.input_email.get()
        funcionario.cpf = tela.input_cpf.get()
        funcionario.cargo = tela.comboboxCargo.get()

    def mostra_janela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

    def _confirma_acao(self, titulo, mensagem):
        return messagebox.askyesno(titulo, mensagem)

    def _get_item_selecionado(self, listbox):
        selecionado = listbox.get(tk.ACTIVE)
        return selecionado[1] if selecionado else None
