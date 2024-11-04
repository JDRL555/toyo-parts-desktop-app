import tkinter as tk
from constants.colors import COLORS

class Pagination(tk.Frame):
  def __init__(self, root, parts_len, page, total, last_page, request_parts):
    super().__init__(root)
    self.root = root
    self.parts_len = parts_len
    self.page = page
    self.total = total
    self.last_page = last_page
    self.request_parts = request_parts
    
  def render(self):
    self.configure(
      width=1100,
      height=50,
      bg=COLORS["primary"],
    )
    
    tk.Button(
      self,
      text="Primera pagina",
      font=("Arial", 12, "bold"),
      bg=COLORS["primary"],
      fg=COLORS["secondary"],
      borderwidth=0,
      cursor="hand2",
      activebackground=COLORS["dark_primary"],
      activeforeground=COLORS["secondary"],
      command=lambda: self.request_parts(1)
    ).grid(row=0, column=0, pady=5, padx=51)
    
    tk.Button(
      self,
      text="Anterior pagina",
      font=("Arial", 12, "bold"),
      bg=COLORS["primary"],
      fg=COLORS["secondary"],
      borderwidth=0,
      cursor="hand2",
      activebackground=COLORS["dark_primary"],
      activeforeground=COLORS["secondary"],
      command=lambda: self.request_parts(self.page - 1 if self.page != 1 else self.page)
    ).grid(row=0, column=1, pady=5, padx=51)
    
    tk.Label(
      self,
      text=f"{self.total} de {self.parts_len}",
      font=("Arial", 12, "bold"),
      bg=COLORS["primary"],
      fg=COLORS["secondary"],
    ).grid(row=0, column=2, pady=5, padx=51)
    
    tk.Button(
      self,
      text="Siguiente pagina",
      font=("Arial", 12, "bold"),
      bg=COLORS["primary"],
      fg=COLORS["secondary"],
      borderwidth=0,
      cursor="hand2",
      activebackground=COLORS["dark_primary"],
      activeforeground=COLORS["secondary"],
      command=lambda: self.request_parts(self.page + 1 if self.page != self.last_page else self.page)
    ).grid(row=0, column=3, pady=5, padx=51)
    
    tk.Button(
      self,
      text="Ultima pagina",
      font=("Arial", 12, "bold"),
      bg=COLORS["primary"],
      fg=COLORS["secondary"],
      borderwidth=0,
      cursor="hand2",
      activebackground=COLORS["dark_primary"],
      activeforeground=COLORS["secondary"],
      command=lambda: self.request_parts(self.last_page)
    ).grid(row=0, column=4, pady=5, padx=51)
    
    self.grid(row=0, column=0, sticky=tk.EW)