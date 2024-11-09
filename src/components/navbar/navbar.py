import tkinter as tk
from constants.colors import COLORS

class Navbar(tk.Frame):
  def __init__(self, root, logo, handle, is_logged = False, handle_payments = None):
    super().__init__(root)
    self.root = root
    self.logo = logo
    self.handle = handle
    self.is_logged = is_logged
    self.handle_payments = handle_payments
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
    )
    buttons_frame.grid(row=0, column=0, sticky=tk.NE, pady=30)
    
    if self.is_logged:
      if self.handle_payments:  
        tk.Button(
          buttons_frame,
          text="Ver compras realizadas",
          font=("Arial", 14),
          borderwidth=0,
          pady=3,
          width=20,
          fg=COLORS["secondary"],
          bg=COLORS["primary"],
          activebackground=COLORS["secondary"],
          activeforeground=COLORS["primary"],
          cursor="hand2",
          command=lambda: self.handle_payments()
        ).grid(row=0, column=0, sticky=tk.E, padx=210)
      
      tk.Button(
        buttons_frame,
        text="Cerrar sesion",
        font=("Arial", 14),
        borderwidth=0,
        pady=3,
        width=15,
        fg=COLORS["secondary"],
        bg=COLORS["primary"],
        activebackground=COLORS["secondary"],
        activeforeground=COLORS["primary"],
        cursor="hand2",
        command=lambda: self.handle()
      ).grid(row=0, column=0, sticky=tk.E, padx=20)
    else:
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
        command=lambda: self.handle(True)
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
        command=lambda: self.handle(False)
      ).grid(row=0, column=0, sticky=tk.E, padx=220)
    
    self.grid(row=0, column=0)