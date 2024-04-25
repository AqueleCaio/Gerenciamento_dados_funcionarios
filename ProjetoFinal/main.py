import tkinter as tk
import funcionario as funcionario
import cargos as cargos

class View_principal():
    def __init__(self, controle, root):
        self.root = root
        self.controle = controle
        
        self.menubar = tk.Menu(self.root)
        self.menu_funcionario = tk.Menu(self.menubar)
        
        self.root.config(menu=self.menubar)
        
        self.menubar.add_cascade(label='Opções', menu=self.menu_funcionario)
        self.menu_funcionario.add_command(label='Cadastrar Funcionário', command=controle.insere_funcionario)
        self.menu_funcionario.add_command(label='Adicionar Cargos', command=controle.insere_cargo)


class Controle_principal():
    def __init__(self):
        self.root = tk.Tk()
        
        self.controle_funcionario = funcionario.Controle_funcionario()
        self.controle_cargos = cargos.Controle_cargos()
        
        self.root.title('§')
        self.root.geometry('300x250')
        self.root.resizable(False, False)
        
        self.view = View_principal(self, self.root)
        
        self.root.mainloop()
        
    def insere_funcionario(self):
        self.controle_funcionario.insere_funcionario()
        
    def insere_cargo(self):
        self.controle_cargos.insere_cargo()
        
if __name__ == '__main__':
    exec = Controle_principal()
