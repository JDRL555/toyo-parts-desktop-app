import tkinter as tk
from tkinter import messagebox

from constants.colors import COLORS 

from utils.report import Report

from controllers import parts as part_controller
from controllers import payments as payment_controller

class ReportWindow(tk.Toplevel):
  def __init__(self, root, logo):
    super().__init__(root)
    self.root = root
    self.logo = logo
    self.propagate(False)    
    
    self.report = Report()
    
    self.report_info = {
      "Partes": {
        "report_of": "Partes",
        "cols": ["ID", "Código", "Cantidad", "Descripción", "Costo", "Precio", "Inventario", "Marca", "Categoria"],
        "rows": part_controller.get_all_parts()
      },
      "Pagos realizados": {
        "report_of": "Pagos realizados",
        "cols": ["ID", "Código de la parte", "Descripción de la parte", "Nombre del cliente", "Fecha de compra"],
        "rows": payment_controller.get_all_payments()
      }
    }
    
    self.title = "Crea una parte"
    self.geometry("600x500")
    self.resizable(False, False)
    self.wm_iconphoto(True, self.logo, self.logo)
    
    self.protocol("WM_DELETE_WINDOW", self.on_close)
    
  def on_close(self):
    self.root.deiconify()
    self.destroy()
    
  def on_report(self, report_of):
    data = self.report_info[report_of]
    
    exported = self.report.export_pdf(data)
    
    if not exported:
      messagebox.showerror("ERROR", "No se pudo exportar en PDF, intente mas tarde")
    else:
      messagebox.showinfo("EXPORTADO", "El reporte fue exportado exitosamente")
    
  def render(self):  
    self.configure(
      bg=COLORS["primary"],
    )  
    
    tk.Label(
      self,
      text=f"Crea un reporte en PDF",
      width=38,
      justify="center",
      font=("Arial", 18),
      bg=COLORS["primary"],
      fg=COLORS["secondary"],
      padx=30,
    ).grid(row=0, column=0, sticky=tk.NW, padx=8, pady=20)
    
    buttons_frame = tk.Frame(
      self,
      width=500,
      height=400,
      bg=COLORS["secondary"],
      pady=10
    )
    buttons_frame.grid_propagate(False)
    buttons_frame.grid(row=1, column=0)
    
    
    tk.Button(
      buttons_frame,
      text="Crear reporte de partes",
      font=("Arial", 18),
      borderwidth=0,
      bg=COLORS["primary"],
      fg=COLORS["secondary"],
      padx=20,
      width=25,
      cursor="hand2",
      command=lambda: self.on_report("Partes")
    ).grid(row=0, column=0, sticky=tk.NW, padx=50, pady=10)
    
    tk.Button(
      buttons_frame,
      text="Crear reporte de pagos",
      font=("Arial", 18),
      borderwidth=0,
      bg=COLORS["primary"],
      fg=COLORS["secondary"],
      padx=20,
      width=25,
      cursor="hand2",
      command=lambda: self.on_report("Pagos realizados")
    ).grid(row=1, column=0, sticky=tk.NW, padx=50, pady=10)
