import tkinter as tk
from constants.colors import COLORS
from components.navbar.navbar import Navbar
from components.table.table import Table

class ClientWindow(tk.Toplevel):
  def __init__(self, root, logo, user):
    super().__init__(root)
    self.root = root
    self.logo = logo
    self.user = user
    self.propagate(False)
    
    self.welcome = f"Bievenido, {'administrador' if self.user['role'] == 'administrador' else ''} {self.user["fullname"]}"
    
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
      "id": "ID",
      "code": "Código",
      "description": "Descripción",
      "brand": "Marca",
      "price": "Precio",
      "category": "Categoria"
    }).render()