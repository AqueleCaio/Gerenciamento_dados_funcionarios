import tkinter as tk
from tkinter import PhotoImage
import funcionario as funcionario
import cargo as cargo

class View_principal():
    def __init__(self, controle, root):
        self.root = root
        self.controle = controle
        
        # Configuração da barra de menu
        self.menubar = tk.Menu(self.root)
        self.menu_funcionario = tk.Menu(self.menubar)
        
        self.root.config(menu=self.menubar)
        
        '''
        Será usado para criar outras opções:
        
        self.menubar.add_cascade(label='Opções', menu=self.menu_funcionario)
        self.menu_funcionario.add_command(label='Cadastrar Funcionário', command=controle.insere_funcionario)
        self.menu_funcionario.add_command(label='Adicionar Cargos', command=controle.insere_cargo)
        ''' 
        
        # Carregar a imagem
        self.add_user_image = PhotoImage(file='imagens/add-user-32.png')
        self.add_function_image = PhotoImage(file='imagens/function-32.png')
        
        # Criar o frame para os botões
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=35)
        
        # Botão para cadastrar funcionário
        self.btn_cadastrar_funcionario = tk.Button(
            self.button_frame, 
            image=self.add_user_image, 
            command=controle.insere_funcionario,
            cursor='hand2'
        )
        self.btn_cadastrar_funcionario.grid(row=0, column=0, padx=10)
        
        self.lbl_cadastrar_funcionario = tk.Label(self.button_frame, text="Cadastrar Funcionário")
        self.lbl_cadastrar_funcionario.grid(row=1, column=0, padx=10)
        
        # Botão para adicionar cargos
        self.btn_adicionar_cargos = tk.Button(
            self.button_frame, 
            image=self.add_function_image, 
            command=controle.insere_cargo,
            cursor='hand2'
            
        )
        self.btn_adicionar_cargos.grid(row=0, column=1, padx=10)
        
        self.lbl_adicionar_cargos = tk.Label(self.button_frame, text="Adicionar Cargos")
        self.lbl_adicionar_cargos.grid(row=1, column=1, padx=10)


class Controle_principal():
    def __init__(self):
        self.root = tk.Tk()
        
        self.controle_funcionario = funcionario.Controle_funcionario()
        self.controle_cargos = cargo.Controle_cargos()
        
        self.root.title('§')
        self.root.geometry('400x150')  # Ajustar tamanho da janela para caber os botões
        self.root.resizable(False, False)
        
        self.view = View_principal(self, self.root)
        
        self.root.mainloop()
        
    def insere_funcionario(self):
        self.controle_funcionario.insere_funcionario()
        
    def insere_cargo(self):
        self.controle_cargos.insere_cargo()
        
if __name__ == '__main__':
    exec = Controle_principal()