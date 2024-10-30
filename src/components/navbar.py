import tkinter as tk
from constants.colors import COLORS

class Navbar(tk.Frame):
  def __init__(self, root, logo):
    super().__init__(root)
    self.root = root
    self.logo = logo
    self.propagate(False)
    
  def render(self):
    self.configure(
      width=1200,
      height=100,
      bg=COLORS["secondary"]
    )
    
    logo_frame = tk.Frame(
      self.root,
      width=600,
      height=100,
      bg=COLORS["secondary"]
    )
    logo_frame.grid(row=0, column=0, sticky=tk.NW)
    
    logo = tk.Label(
      logo_frame,
      image=self.logo
    )
    logo.grid(row=0, column=0)
    
    buttons_frame = tk.Frame(
      self.root,
      width=600, 
      height=100,
      padx=10,
      bg=COLORS["secondary"]
    ).grid(row=0, column=0, sticky=tk.NE)
    
    tk.Button(
      buttons_frame,
      text="Iniciar sesión",
      font=("Arial", 14),
      borderwidth=0,
      pady=3,
      width=15,
      fg=COLORS["secondary"],
      bg=COLORS["primary"],
      activebackground=COLORS["secondary"],
      activeforeground=COLORS["primary"],
      cursor="hand2",
    ).grid(row=0, column=0, sticky=tk.E, padx=20)
    
    tk.Button(
      buttons_frame,
      text="Regitrarse",
      font=("Arial", 14),
      borderwidth=0,
      pady=3,
      width=15,
      fg=COLORS["secondary"],
      bg=COLORS["primary"],
      activebackground=COLORS["secondary"],
      activeforeground=COLORS["primary"],
      cursor="hand2",
    ).grid(row=0, column=0, sticky=tk.E, padx=220)
    
    self.grid(row=0, column=0)