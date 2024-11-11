import tkinter as tk
from tkinter import messagebox
from constants.colors import COLORS

from controllers.users import create_user
class RegisterForm(tk.Frame):
  def __init__(self, root, handle_login):
    super().__init__(root)
    self.root = root
    self.handle_login = handle_login
    self.propagate(False)
    
    self.name_var = tk.StringVar()
    self.email_var = tk.StringVar()
    self.pass_var = tk.StringVar()
    
  def on_submit(self):
    fullname = self.name_var.get()
    email = self.email_var.get()
    password = self.pass_var.get()
    
    response, code = create_user({
      "fullname": fullname,
      "email": email,
      "password": password,
    })
    
    if code != 201:
      messagebox.showerror("Error", response["message"])
    else:
      messagebox.showinfo("Sucess", response['message'])
      self.handle_login(True)
      
      self.name_var.set("")
      self.email_var.set("")
      self.pass_var.set("")
      

  def render(self):
    self.configure(
      width=500,
      height=370,
      bg=COLORS["secondary"]
    )
    
    title = tk.Label(
      self,
      text="Registrate",
      font=("Arial", 18),
      width=36,
      bg=COLORS["secondary"],
      justify="center"
    )
    title.grid(row=0, column=0, sticky=tk.NE, pady=10)
    
    # seccion de inputs
    name_label = tk.Label(
      self,
      text="Nombre completo",
      font=("Arial", 14),
      bg=COLORS["secondary"],
    )
    name_label.grid(row=1, column=0, sticky=tk.W, pady=10, padx=20)
    
    name_input = tk.Entry(
      self,
      bg=COLORS["secondary"],
      width=40,
      font=("Arial", 14),
      textvariable=self.name_var
    )
    name_input.grid(row=2, column=0, sticky=tk.W, padx=25)
    
    email_label = tk.Label(
      self,
      text="Correo",
      font=("Arial", 14),
      bg=COLORS["secondary"],
    )
    email_label.grid(row=3, column=0, sticky=tk.W, pady=10, padx=20)
    
    email_input = tk.Entry(
      self,
      bg=COLORS["secondary"],
      width=40,
      font=("Arial", 14),
      textvariable=self.email_var
    )
    email_input.grid(row=4, column=0, sticky=tk.W, padx=25)
    
    # clave
    pass_label = tk.Label(
      self,
      text="Clave",
      font=("Arial", 14),
      bg=COLORS["secondary"],
    )
    pass_label.grid(row=5, column=0, sticky=tk.W, pady=10, padx=20)
    
    pass_input = tk.Entry(
      self,
      bg=COLORS["secondary"],
      width=40,
      show="*",
      font=("Arial", 14),
      textvariable=self.pass_var
    )
    pass_input.grid(row=6, column=0, sticky=tk.W, padx=25)
    
    button = tk.Button(
      self,
      text="Registrate",
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
    button.grid(row=7, column=0, sticky=tk.W, padx=25, pady=20)
    
    self.grid_propagate(False)
    self.grid(row=1, column=0, sticky=tk.NE, pady=50, padx=40)