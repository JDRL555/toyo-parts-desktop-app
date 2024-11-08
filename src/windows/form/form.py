import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from constants.colors import COLORS 

from utils.validate import validate_part
from utils.database import session

from models.Part import Brands, Categories

from controllers import parts as part_controller

from controllers import brands as brand_controller
from controllers import categories as category_controller

class FormWindow(tk.Toplevel):
  def __init__(self, root, logo, request_parts, part = None):
    super().__init__(root)
    self.root = root
    self.logo = logo
    self.part = part
    self.request_parts = request_parts
    self.propagate(False)    
    
    self.title = "Crea una parte"
    self.geometry("1000x500")
    self.resizable(False, False)
    self.wm_iconphoto(True, self.logo, self.logo)
    
    self.brands = brand_controller.get_brands()
    self.categories = category_controller.get_categories()
    
    self.vars = []
        
    self.data = {
      "code": "Código", 
      "description": "Descripción", 
      "quantity": "Cantidad", 
      "brand": "Marca", 
      "cost": "Costo", 
      "price": "Precio", 
      "inventory": "Inventario", 
      "category": "Categoría", 
    }
    
    self.protocol("WM_DELETE_WINDOW", self.on_close)
    
  def on_close(self):
    self.root.deiconify()
    self.destroy()
    
  def on_submit(self):
    part = {}
    for i, col in enumerate(self.data.keys()):
      try:
        part[col] = self.vars[i].get()
      except tk.TclError:
        messagebox.showerror(col, f"{"La" if self.data[col] == "Cantidad" else "La"} {self.data[col]} debe ser numerico")
        return
    if not self.part:
      errors = validate_part(part)
      
      if len(errors) != 0:
        for error in errors:
          messagebox.showerror(error["field"], error["message"])
        return
      
      brand = session.query(Brands).filter_by(name = part["brand"]).first()
      category = session.query(Categories).filter_by(name = part["category"]).first()
    else:
      brand = session.query(Brands).filter_by(name = self.part["brand"]).first()
      category = session.query(Categories).filter_by(name = self.part["category"]).first()

    part["brand_id"] = brand.id
    part["category_id"] = category.id
    
    del part["brand"]
    del part["category"]
    
    if not self.part:
      result, code = part_controller.create_part(part)
      success_code = 201
    else:
      result, code = part_controller.edit_part(self.part["id"], part)
      success_code = 200
    
    if code != success_code:
      messagebox.showerror(
        "ERROR", 
        result["message"]
      )
    else:
      messagebox.showinfo(
        "CREADO" if not self.part else "EDITADO", 
        result["message"]
      )
      self.request_parts(page=1)
      self.on_close()
    
  def render(self):  
    self.configure(
      bg=COLORS["primary"],
    )  
    
    tk.Label(
      self,
      text=f"{"Crea" if not self.part else "Edita"} una parte",
      width=67,
      justify="center",
      font=("Arial", 18),
      bg=COLORS["primary"],
      fg=COLORS["secondary"],
      padx=30,
    ).grid(row=0, column=0, sticky=tk.NW, padx=10, pady=20)
    
    inputs_frame = tk.Frame(
      self,
      width=800,
      borderwidth=1,
      bg=COLORS["secondary"],
      relief="groove",
      pady=20,
    )
    inputs_frame.grid(row=1, column=0, padx=40)
    
    for index, label in enumerate(self.data.values()):
      var = tk.StringVar()
      
      if self.part:
        values = [value for key, value in self.part.items() if key != "id"]
        value = values[index]
        var.set(value)
      
      divisor = 5 if index < 4 else 4 
      
      row = (2 * (index % divisor) + 1) - 1
      col = 0 if index < 4 else 1

      tk.Label(
        inputs_frame,
        text=label,
        font=("Arial", 14),
        bg=COLORS["secondary"],
      ).grid(row=row, column=col, sticky=tk.NW, padx=20, pady=5)
      
      if label == "Marca" or label == "Categoría":
        values = self.brands if label == "Marca" else self.categories
        ttk.Combobox(
          inputs_frame,
          width=34,
          font=("Arial", 14),
          state="readonly",
          values=[value["name"] for value in values],
          textvariable=var
        ).grid(row=row+1, column=col, sticky=tk.NW, padx=20, pady=5)
      else:
        tk.Entry(
          inputs_frame,
          width=35,
          font=("Arial", 14),
          textvariable=var,
          bg=COLORS["secondary"],
        ).grid(row=row+1, column=col, sticky=tk.NW, padx=20, pady=5)
      
      self.vars.append(var)
    
    tk.Button(
      inputs_frame,
      text="Crear" if not self.part else "Editar",
      font=("Arial", 14),
      borderwidth=0,
      bg=COLORS["primary"],
      fg=COLORS["secondary"],
      padx=20,
      cursor="hand2",
      command=self.on_submit
    ).grid(row=8, column=0, sticky=tk.NW, padx=16, pady=10)
