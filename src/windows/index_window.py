import tkinter as tk
from constants.colors import COLORS
from components.navbar import Navbar

class MainWindow(tk.Frame):
  def __init__(self, root, logo):
    super().__init__(root)
    self.root = root
    self.logo = logo
    self.propagate(False)
    
  def render(self):
    self.configure(
      width=1200,
      height=800,
      bg=COLORS["primary"]
    )
    
    Navbar(self.root, self.logo).render()
    
    # tk.Label(
    #   self.root, 
    #   text="Bievenido",
    #   font=("Arial", 16),
    #   width=100,
    #   bg=COLORS["primary"]
    # ).grid(row=1, column=0)
    
    self.grid()