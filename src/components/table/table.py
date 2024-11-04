import tkinter as tk
from constants.colors import COLORS

from controllers import parts as parts_controller

from .sections.pagination import Pagination

class Table(tk.Frame):
  def __init__(self, root, columns):
    super().__init__(root)
    self.root = root
    self.columns = columns
    self.propagate(False)
    
    self.page = 1
    self.last_page = 1
    self.total = 29 
    self.len_last_parts = 29
    self.parts = parts_controller.get_parts()
    self.parts_len = parts_controller.get_parts_len()
    
    
    self.wraplength = [
      20,
      200,
      400,
      300,
      50,
      200
    ]
    
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
      width=1100,
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
        text=col,
        font=("Arial", 11, "bold"),
      ).grid(row=0, column=index, padx=40, sticky=tk.N)
      
    for col_index, col_key in enumerate(self.columns.keys()):
      for row_index, part in enumerate(self.parts):
        global text
        if col_key == "brand" or col_key == "category":
          text = part[col_key]["name"]
        else:
          text = part[col_key]
          
        tk.Label(
          self.table_frame,
          text=text,
          wraplength=self.wraplength[col_index],
          justify="center",
          font=("Arial", 11)
        ).grid(row=row_index + 1, column=col_index, sticky=tk.N, pady=5)
    
  def request_parts(self, page: int):
    self.pagination.destroy()
    
    self.parts = parts_controller.get_parts(page)
    self.page = page
    self.len_last_parts = len(parts_controller.get_parts(page=page - 1)) if page != 1 else 29
    
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
    
  def render(self):
    self.grid(row=2, column=0, sticky=tk.N, pady=20)