import tkinter as tk
from constants.colors import COLORS

from controllers import parts as parts_controller

from .sections.pagination import Pagination

class Table(tk.Frame):
  def __init__(self, root, columns, col_padx, is_admin = False):
    super().__init__(root)
    self.root = root
    self.columns = columns
    self.col_padx = col_padx
    self.is_admin = is_admin
    self.propagate(False)
    
    self.counter = 1
    
    self.page = 1
    self.last_page = 1
    self.total = 29 
    self.len_last_parts = 29
    self.parts = parts_controller.get_parts(is_admin=self.is_admin)
    self.parts_len = parts_controller.get_parts_len(is_admin=self.is_admin)
    
    self.pagination = Pagination(
      self, 
      self.parts_len,
      self.page, 
      self.total,
      self.last_page,
      self.request_parts
    )
    self.pagination.render()
    
    canvas = tk.Canvas(
      self,
      width=1150,
      height=350,
      borderwidth=2,
      highlightcolor="#444",
      relief="groove",
    )
    
    scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    self.table_frame = tk.Frame(canvas)
    
    self.table_frame.bind(
      "<Configure>",
      lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
      )
    )
    
    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
    
    canvas.create_window((0,0), window=self.table_frame, anchor="w")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.grid(row=1, column=0)
    scrollbar.grid(row=1, column=1, sticky=tk.NS)
    
    self.load_table_content()
    
        
  def load_table_content(self):
    for widget in self.table_frame.winfo_children():
      widget.destroy()
    
    for index, col in enumerate(self.columns.values()):
      tk.Label(
        self.table_frame,
        text=col[0],
        font=("Arial", 11, "bold"),
      ).grid(row=0, column=index, padx=self.col_padx, sticky=tk.N)
      
    for col_index, col_key in enumerate(self.columns.keys()):
      for row_index, part in enumerate(self.parts):
        global text
        global row
        
        if col_key in ["edit", "delete"]:
          row = tk.Button(
            self.table_frame,
            text=self.columns[col_key][0],
            wraplength=list(self.columns.values())[col_index][1],
            borderwidth=0,
            bg=COLORS["primary"],
            fg=COLORS["secondary"],
            justify="center",
            cursor="hand2",
            font=("Arial", 11),
          )
        else:  
          if col_key in ["brand", "category"]:
            text = part[col_key]["name"]
          else:
            text = part[col_key]
            
          row = tk.Label(
            self.table_frame,
            text=text,
            wraplength=list(self.columns.values())[col_index][1],
            justify="center",
            font=("Arial", 11),
          )
        
        row.grid(row=row_index + 1, column=col_index, sticky=tk.N, pady=5)
    
  def request_parts(self, page: int):
    self.pagination.destroy()
    
    self.parts = parts_controller.get_parts(page, is_admin=self.is_admin)
    self.page = page
    self.len_last_parts = len(parts_controller.get_parts(page=page - 1, is_admin=self.is_admin)) if page != 1 else 29
    
    division = self.parts_len / 29
    residuo = self.parts_len % 29
    self.last_page = int(division) + 1 if residuo != 0 else int(division)
    self.total = 29 if self.page == 1 else ((self.page - 1) * self.len_last_parts) + len(self.parts)
    
    self.pagination = Pagination(
      self, 
      self.parts_len,
      self.page, 
      self.total,
      self.last_page,
      self.request_parts
    )
    self.pagination.render()
    
    self.load_table_content()
    
  def open_admin_options(self, part):
    print(part)
    def on_delete(options):
      self.counter = 1
      options.destroy()
      
    if self.counter == 1:
      options = tk.Toplevel(
        self,
        width=200,
        height=100
      )
      options.wait_visibility()
      
      x = self.winfo_x() + self.winfo_width()//2 - options.winfo_width()//2
      y = self.winfo_y() + self.winfo_height()//2 - options.winfo_height()//2
      
      options.geometry(f"+{x}+{y}")
      options.grid_propagate(False)
      options.resizable(False, False)
      
      tk.Button(
        options,
        text="Editar",
        borderwidth=0,
        width=22,
        font=("Arial", 12),
        fg=COLORS["secondary"],
        bg=COLORS["primary"],
        pady=12,
        cursor="hand2",
      ).grid(row=0, column=0)
      
      tk.Button(
        options,
        text="Eliminar",
        borderwidth=0,
        width=22,
        font=("Arial", 12),
        fg=COLORS["secondary"],
        bg=COLORS["primary"],
        pady=12,
        cursor="hand2",
      ).grid(row=1, column=0)
      
      self.counter = 2
      options.protocol("WM_DELETE_WINDOW", lambda: on_delete(options))
    
  def render(self):
    self.grid(row=2, column=0, sticky=tk.N, pady=20)