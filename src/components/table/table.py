import tkinter as tk
from tkinter import messagebox

from constants.colors import COLORS

from controllers import parts as parts_controller

from windows.form.form import FormWindow

from .sections.pagination import Pagination

class Table(tk.Frame):
  def __init__(self, root, columns, col_padx, is_admin = False, logo = None):
    super().__init__(root)
    self.root = root
    self.columns = columns
    self.col_padx = col_padx
    self.is_admin = is_admin
    self.logo = logo
    self.propagate(False)
    
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
    
  def on_edit(self, row_index: int):
    key_order = ["id", "code", "description", "quantity", "brand", "cost", "price", "inventory", "category"]
    
    part = self.parts[row_index]
    part["brand"] = part["brand"]["name"]
    part["category"] = part["category"]["name"]
    
    part_sorted = {k: part[k] for k in key_order}
    
    FormWindow(self.root, self.logo, self.request_parts, part_sorted).render()
    self.root.withdraw()
    
  def on_delete(self, row_index: int):
    part = self.parts[row_index]
    
    accept = messagebox.askyesno("Seguro?", f"Esta seguro de eliminar {part["description"]}?")
    
    if accept:
      _, code = parts_controller.delete_part(part["id"])
      if code != 200:
        messagebox.showerror("ERROR", "La parte no se encontro")
      else:
        messagebox.showinfo("ELIMINADO", "La parte fue eliminada exitosamente")
        self.request_parts(page=1)
        
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
        if col_key in ["edit", "delete"]:
          
          if col_key == "edit":
            row = tk.Button(
              self.table_frame,
              text=self.columns[col_key][0],
              wraplength=list(self.columns.values())[col_index][1],
              borderwidth=0,
              bg=COLORS["edit"],
              fg=COLORS["secondary"],
              justify="center",
              cursor="hand2",
              command=lambda idx=row_index: self.on_edit(idx),
              font=("Arial", 11),
            )
          else:
            row = tk.Button(
              self.table_frame,
              text=self.columns[col_key][0],
              wraplength=list(self.columns.values())[col_index][1],
              borderwidth=0,
              bg=COLORS["primary"],
              fg=COLORS["secondary"],
              justify="center",
              cursor="hand2",
              command=lambda idx=row_index: self.on_delete(idx),
              font=("Arial", 11),
            )

        else:  
          if col_key in ["brand", "category"]:
            text = part[col_key]["name"]
          else:
            text = part[col_key]
            
          if part["quantity"] == 0:
            color = COLORS["primary"]
          else:
            color = "#222"
            
          row = tk.Label(
            self.table_frame,
            text=0 if text == None else text,
            wraplength=list(self.columns.values())[col_index][1],
            justify="center",
            font=("Arial", 11),
            fg=color
          )
        
        row.grid(row=row_index + 1, column=col_index, sticky=tk.N, pady=5)
    
  def request_parts(self, page: int):
    self.pagination.destroy()
    
    self.parts = parts_controller.get_parts(page, is_admin=self.is_admin)
    self.parts_len = parts_controller.get_parts_len(is_admin=self.is_admin)
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
    
  def render(self):
    self.grid(row=2, column=0, sticky=tk.N, pady=20)