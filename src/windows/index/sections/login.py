import tkinter as tk
from tkinter import messagebox
from constants.colors import COLORS

from controllers.auth import login

from windows.client.client import ClientWindow

class LoginForm(tk.Frame):
  def __init__(self, root, logo):
    super().__init__(root)
    self.root = root
    self.logo = logo
    self.propagate(False)
    
    self.email_var = tk.StringVar()
    self.pass_var = tk.StringVar()
    
  def on_submit(self):
    email = self.email_var.get()
    password = self.pass_var.get()
    
    response, code = login(email=email, password=password)
    
    if code != 200:
      messagebox.showerror("Error", response["message"])
    else:
      ClientWindow(self.root, self.logo, response["user"]).render()
      self.root.withdraw()
      
      self.email_var.set("")
      self.pass_var.set("")

  def render(self):
    self.configure(
      width=500,
      height=300,
      bg=COLORS["secondary"]
    )
    
    title = tk.Label(
      self,
      text="Iniciar sesión",
      font=("Arial", 18),
      width=36,
      bg=COLORS["secondary"],
      justify="center"
    )
    title.grid(row=0, column=0, sticky=tk.NE, pady=10)
    
    email_label = tk.Label(
      self,
      text="Correo",
      font=("Arial", 14),
      bg=COLORS["secondary"],
    )
    email_label.grid(row=1, column=0, sticky=tk.W, pady=10, padx=20)
    
    email_input = tk.Entry(
      self,
      bg=COLORS["secondary"],
      width=40,
      font=("Arial", 14),
      textvariable=self.email_var
    )
    email_input.grid(row=2, column=0, sticky=tk.W, padx=25)
    
    # clave
    pass_label = tk.Label(
      self,
      text="Clave",
      font=("Arial", 14),
      bg=COLORS["secondary"],
    )
    pass_label.grid(row=3, column=0, sticky=tk.W, pady=10, padx=20)
    
    pass_input = tk.Entry(
      self,
      bg=COLORS["secondary"],
      width=40,
      show="*",
      font=("Arial", 14),
      textvariable=self.pass_var
    )
    pass_input.grid(row=4, column=0, sticky=tk.W, padx=25)
    
    button = tk.Button(
      self,
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
      command=self.on_submit
    )
    button.grid(row=5, column=0, sticky=tk.W, padx=25, pady=20)
    
    self.grid_propagate(False)
    self.grid(row=1, column=0, sticky=tk.NE, pady=50, padx=40)