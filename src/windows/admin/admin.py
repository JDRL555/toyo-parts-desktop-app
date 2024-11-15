import tkinter as tk
from constants.colors import COLORS
from components.navbar.navbar import Navbar
from components.table.table import Table

from windows.form.form import FormWindow
from windows.payments.payments import PaymentsWindow
from windows.reports.report import ReportWindow

from utils.controller import Controller

class AdminWindow(tk.Toplevel):
  def __init__(self, root, logo, user):
    super().__init__(root)
    self.root = root
    self.logo = logo
    self.user = user
    self.is_admin = user["role"] == "administrador"
    
    self.controller = Controller()
    self.propagate(False)
    
    self.handle_admin = {
      "payments": self.on_payments_click,
      "reports": self.on_reports_click
    }
    
    self.cols = {
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
    }
    
    self.table = Table(
      self, 
      self.cols, 
      col_padx=15, 
      controller=self.controller,
      user=self.user, 
      logo=self.logo,
    )
    
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
    FormWindow(self, self.logo, self.table.request_data).render()
    self.withdraw()
    
  def on_close_payments(self):
    AdminWindow(self.root, self.logo, self.user).render()
    
  def on_payments_click(self):
    PaymentsWindow(self.root, self.logo, self.user, self.on_close_payments).render()
    self.destroy()
    
  def on_reports_click(self):
    ReportWindow(self, self.logo).render()
    self.withdraw()
    
    
  def render(self):    
    Navbar(self, self.logo, self.on_sign_out, is_logged=True, handle_admin=self.handle_admin).render()
    
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
    
    self.table.render()