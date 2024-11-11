import tkinter as tk

from components.table.table import Table

from controllers import payments as payment_controller

class Controller:
  def get(self, page = 1, is_admin = False): 
    return payment_controller.get_payments(page=page, is_admin=is_admin)
  
  def get_len(self, is_admin = False):
    return payment_controller.get_payments_len(is_admin=is_admin)

class PaymentsWindow(tk.Toplevel):
  def __init__(self, root, logo, user, on_close):
    super().__init__(root)
    self.root = root
    self.logo = logo
    self.user = user
    self.on_close = on_close
    self.controller = Controller()
    self.propagate(False)
    
    self.cols = {
      "id": ["ID", 40],
      "part.code": ["Código de la parte", 200],
      "part.description": ["Descripción de la parte", 300],
      "user.fullname": ["Nombre del cliente", 200],
      "paid_at": ["Fecha de compra", 200],
    }
    
    self.title = "Pagos realizados"
    self.geometry("1200x600")
    self.resizable(False, False)
    self.wm_iconphoto(True, self.logo, self.logo)
    
    self.protocol("WM_DELETE_WINDOW", self.on_close_window)
    
  def on_close_window(self):
    self.on_close()
    self.destroy()
    
  def render(self):    
    self.configure(
      padx=20
    )
    tk.Label(
      self,
      text="Pagos realizados",
      font=("Arial", 18)
    ).grid(row=0, column=0, sticky=tk.NW, padx=10, pady=10)
    
    Table(
      self,
      self.cols,
      col_padx=40, 
      controller=self.controller,
      user=self.user,
      readonly=True
    ).render()