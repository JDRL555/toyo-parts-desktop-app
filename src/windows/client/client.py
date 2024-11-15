import tkinter as tk
from constants.colors import COLORS

from components.navbar.navbar import Navbar
from components.table.table import Table

from utils.controller import Controller
class ClientWindow(tk.Toplevel):
  def __init__(self, root, logo, user):
    super().__init__(root)
    self.root = root
    self.logo = logo
    self.user = user
    self.controller = Controller()
    self.propagate(False)
    
    self.welcome = f"Bievenido, cliente {self.user["fullname"]}"
    
    self.title = self.welcome
    self.geometry("1200x600")
    self.resizable(False, False)
    self.wm_iconphoto(True, self.logo, self.logo)
    
    self.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())
    
  def on_sign_out(self):
    self.root.deiconify()
    self.destroy()
    
  def render(self):    
    # componentes
    Navbar(self, self.logo, self.on_sign_out, is_logged=True).render()
    
    tk.Label(
      self,
      text=self.welcome,
      font=("Arial", 18)
    ).grid(row=1, column=0, sticky=tk.NW, padx=10, pady=10)
    
    Table(self, {
        "id": ["ID", 40],
        "code": ["Código", 200],
        "description": ["Descripción", 300],
        "brand": ["Marca", 300],
        "price": ["Precio", 50],
        "category": ["Categoria", 200],
        "buy": ["Comprar", 100]
      }, 
      col_padx=40, 
      controller=self.controller,
      user=self.user
    ).render()