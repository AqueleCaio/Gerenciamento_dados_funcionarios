import requests
import tkinter as tk
from tkinter import messagebox
import pickle, os.path

class Cargos:
    def __init__(self, nome, salario, descricao):
        self.nome = nome
        self.salario = salario
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome

    @property
    def salario(self):
        return self.__salario

    @property
    def descricao(self):
        return self.__descricao

    @nome.setter
    def nome(self, nome):
        if nome == '':
            raise ValueError('Nome não pode ser vazio')

        elif any(char.isdigit() for char in nome):
            raise ValueError('Nome não pode conter números')
        
        else:
            self.__nome = nome
            
    @salario.setter
    def salario(self, salario):
        if salario == '':
            raise ValueError('Salário não pode ser vazio')

        elif not str(salario).isdigit():
            raise ValueError('Salário deve ser um número')

        else:
            self.__salario = salario


class View_cargos(tk.Toplevel): 
    def __init__(self, controle, lista_cargo): 
        tk.Toplevel.__init__(self)
        self.controle = controle
                
        self.title('Cargos')
        self.geometry('550x350')
        self.configure(bg='light blue')
        self.resizable(False, False)

        self.frame_left = tk.Frame(self, bg='light blue', borderwidth=1, relief='solid') # Frame esquerdo
        self.frame_right = tk.Frame(self, bg='light blue') # Frame direito

        self.titulo_left = tk.Label(self.frame_left, text='Insira um cargo', bg='light blue')
        self.titulo_left.config(font=('Arial', 13, 'bold'))
        self.titulo_right = tk.Label(self.frame_right, text='Lista de Cargos', bg='light blue')
        self.titulo_right.config(font=('Arial', 13, 'bold'))

        self.frame_inputs = tk.Frame(self.frame_left, bg='light blue')
        
        self.nome = tk.Label(self.frame_inputs, text='Cargo', bg='light blue')
        self.salario = tk.Label(self.frame_inputs, text='Salário', bg='light blue')
        self.descricao = tk.Label(self.frame_inputs, text='Descrição', bg='light blue')

        self.input_nome = tk.Entry(self.frame_inputs)
        self.input_salario = tk.Entry(self.frame_inputs, width=10)
        self.input_descricao = tk.Text(self.frame_inputs, width=30, height=5)

        self.listbox = tk.Listbox(self.frame_right, width=27, height=14)
        
        self.listbox.bind('<Double-1>', lambda event: controle.on_listbox_select(event, self.listbox))#Passar um metodo double click

        for listbox in lista_cargo:
            self.listbox.insert(tk.END, listbox)

        # Novo frame para os botões
        self.frame_botoes = tk.Frame(self.frame_left, bg='light blue')

        self.botao_adiciona = tk.Button(self.frame_botoes, text='Adicionar', command=controle.enterHandler)
        self.botao_gerar_descricao = tk.Button(self.frame_botoes, text='Gerar Descrição', command=controle.gerar_descricao)
        
        self.botao_deleta = tk.Button(self.frame_right, text='Deletar', command=controle.deleta_cargo)

        # Layout
        self.frame_left.pack(side=tk.LEFT, padx=15, pady=10)
        self.frame_right.pack(side=tk.RIGHT, padx=15, pady=10)

        self.titulo_left.pack(pady=10)
        self.frame_inputs.pack(pady=10, ipadx=10, ipady=10)

        self.nome.grid(row=0, column=0, sticky='w', pady=5)
        self.salario.grid(row=1, column=0, sticky='w', pady=5)
        self.descricao.grid(row=2, column=0, sticky='w', pady=5)
        
        self.input_nome.grid(row=0, column=1, sticky='w', pady=5)
        self.input_salario.grid(row=1, column=1, sticky='w', pady=5)
        self.input_descricao.grid(row=2, column=1, sticky='w', pady=1)

        self.titulo_right.pack(pady=10)
        self.listbox.pack(padx=5, pady=5)
        
        # Layout dos botões no novo frame
        self.frame_botoes.pack(pady=7, fill=tk.X)
        
        self.botao_adiciona.grid(row=0, column=0, padx=(40, 50))  # Espaçamento à direita do primeiro botão
        self.botao_gerar_descricao.grid(row=0, column=1, padx=(50, 0))  # Espaçamento à esquerda do segundo botão


        self.botao_deleta.pack(padx=5, pady=5)



class Controle_cargos:
    def __init__(self):
        if not os.path.isfile('cargos.pickle'):
            self.lista_cargos = []
        else:
            with open('cargos.pickle', 'rb') as file:
                self.lista_cargos = pickle.load(file)
                
    def salva_dados_cargo(self):
        with open('cargos.pickle', 'wb') as file:
            pickle.dump(self.lista_cargos, file)
        
    def insere_cargo(self): 
        lista_cargo = self.get_nome()
        self.cargo = View_cargos(self, lista_cargo)
        
    def enterHandler(self):
        nome = self.cargo.input_nome.get()
        salario = self.cargo.input_salario.get()
        descricao = self.cargo.input_descricao.get('1.0', tk.END)
        
        try:
            if int(salario) < 700:
                raise ValueError('Salário deve ser maior que 800')
            
            else: 
                self.lista_cargos.append(Cargos(nome, salario, descricao))
                listbox = self.cargo.listbox
                listbox.insert(tk.END, nome)
                messagebox.showinfo('Sucesso', 'Cargo Inserido com Sucesso!')
                self.salva_dados_cargo()
                self.clean_text()
            
        except ValueError as erro:
            messagebox.showerror('Erro', erro)
            
    def get_nome(self):
        return [cargo.nome for cargo in self.lista_cargos]
    
    def deleta_cargo(self):
        cargo_sel = self.cargo.listbox.get(tk.ACTIVE)

        if cargo_sel:
            resposta = messagebox.askyesno("Confirmar Exclusão", f"Você realmente deseja deletar o cargo '{cargo_sel}'?")

            if resposta:
                for cargo in self.lista_cargos:
                    if cargo.nome == cargo_sel:
                        self.lista_cargos.remove(cargo)
                        self.salva_dados_cargo()
                        messagebox.showinfo('Sucesso', 'Cargo deletado com sucesso!')
                        self.cargo.listbox.delete(tk.ACTIVE)
                        break
                    
    def mostra_funcionario(self, cargo_sel):
        for cargos in self.lista_cargos:
            if cargo_sel == cargos.nome:
                info_cargo = '\n\n'.join([
                    f'Cargo: {cargos.nome}',
                    f'Salário: R${cargos.salario}',
                    f'Descrição: {cargos.descricao}'
                ])
                messagebox.showinfo('Visualizar Cargo', info_cargo)

    def on_listbox_select(self, event, listbox):
        cargo_sel = listbox.get(tk.ACTIVE)
        self.mostra_funcionario(cargo_sel)

    def clean_text(self):
        self.cargo.input_nome.delete(0, tk.END)
        self.cargo.input_salario.delete(0, tk.END)
        self.cargo.input_descricao.delete('1.0', tk.END)

    def gerar_descricao(self):
        cargo_nome = self.cargo.input_nome.get()
        if not cargo_nome:
            messagebox.showerror("Erro", "Insira o nome do cargo para gerar a descrição.")
            return

        url = f"https://pt.wikipedia.org/api/rest_v1/page/summary/{cargo_nome.replace(' ', '_')}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                descricao = data.get('extract', 'Nenhuma descrição encontrada.')
                self.cargo.input_descricao.delete('1.0', tk.END)
                self.cargo.input_descricao.insert(tk.END, descricao)
            else:
                messagebox.showerror("Erro", f"Erro ao buscar descrição: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao buscar descrição: {e}")
