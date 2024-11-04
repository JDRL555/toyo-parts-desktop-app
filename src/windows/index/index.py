import tkinter as tk
from constants.colors import COLORS
from components.navbar.navbar import Navbar

from .sections.login import LoginForm
from .sections.register import RegisterForm

class MainWindow(tk.Frame):
  def __init__(self, root, logo, local):
    super().__init__(root)
    self.root = root
    self.logo = logo
    self.local = local
    self.propagate(False)
    
    self.login_frame = LoginForm(self.root, self.logo)
    self.register_frame = RegisterForm(self.root, self.handle_login)
    
  def handle_login(self, is_login: bool):
    if is_login:
      self.register_frame.grid_forget()
      self.login_frame.render()
    else:
      self.login_frame.grid_forget()
      self.register_frame.render()
    
  def render(self):
    self.configure(
      width=1200,
      height=800,
      bg=COLORS["primary"]
    )
    
    # componentes
    Navbar(self.root, self.logo, self.handle_login).render()
    
    # frames o marcos de la ventana
    img_frame = tk.Frame(
      self.root,
      width=600,
      height=600,
    )
    img_frame.grid(row=1, column=0, sticky=tk.NW)
    
    # imagen del local
    local_img = tk.Label(
      img_frame,
      borderwidth=0,
      image=self.local
    )
    local_img.grid(row=0, column=0, sticky=tk.W)
    
    # contenido del formulario
    self.login_frame.render()
    
    self.grid(row=1, column=0)