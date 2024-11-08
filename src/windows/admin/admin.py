import tkinter as tk
from constants.colors import COLORS
from components.navbar.navbar import Navbar
from components.table.table import Table

from windows.form.form import FormWindow

class AdminWindow(tk.Toplevel):
  def __init__(self, root, logo, user):
    super().__init__(root)
    self.root = root
    self.logo = logo
    self.user = user
    self.propagate(False)
    
    self.welcome = f"Bievenido, admin {self.user["fullname"]}"
    
    self.title = self.welcome
    self.geometry("1200x600")
    self.resizable(False, False)
    self.wm_iconphoto(True, self.logo, self.logo)
    
    self.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())
    
  def on_sign_out(self):
    self.root.deiconify()
    self.destroy()
    
  def on_create_click(self):
    FormWindow(self, self.logo).render()
    self.withdraw()
    
  def render(self):    
    Navbar(self, self.logo, self.on_sign_out, is_logged=True).render()
    
    tk.Label(
      self,
      text=self.welcome,
      font=("Arial", 18)
    ).grid(row=1, column=0, sticky=tk.NW, padx=10, pady=10)
    
    tk.Button(
      self,
      text="Nueva parte",
      font=("Arial", 14),
      borderwidth=0,
      bg=COLORS["create"],
      cursor="hand2",
      command=self.on_create_click
    ).grid(row=1, column=0, sticky=tk.NE, padx=14, pady=10)
    
    Table(self, {
      "id": ["ID", 40],
      "code": ["Código", 200],
      "description": ["Descripción", 200],
      "quantity": ["Cantidad", 20],
      "brand": ["Marca", 200],
      "cost": ["Costo", 40],
      "price": ["Precio", 50],
      "inventory": ["Inventario", 40],
      "category": ["Categoria", 100],
      "edit": ["Editar", 100],
      "delete": ["Eliminar", 100],
    }, col_padx=15, is_admin=True, logo=self.logo).render()