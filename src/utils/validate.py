from email_validator import validate_email, EmailNotValidError
from .database import session
from models.Part import Parts, Brands, Categories

def is_email_valid(email: str):
  try:
    validate_email(email)
    return True
  except EmailNotValidError:
    return False
  
def validate_part(part: dict):
  required_fields = ['code', 'quantity', 'description', 'cost', 'price', 'inventory', 'brand', 'category']
  
  if not all(part.get(field) for field in required_fields):
    return [{
      "field": "ERROR",
      "message": "Faltan campos por llenar"
    }], None, None
  
  errors = []
    
  try:
    part["quantity"] = int(part.get("quantity"))
  except:
    errors.append({
      "field": "Cantidad",
      "message": "La cantidad debe ser un número entero"
    })
    
  try:
    part["price"] = float(part.get("price"))
  except:
    errors.append({
      "field": "Precio",
      "message": "El precio debe ser un número"
    })
    
  try:
    part["cost"] = float(part.get("cost"))
  except:
    errors.append({
      "field": "Costo",
      "message": "El costo debe ser un número"
    })
    
  try:
    part["inventory"] = float(part.get("inventory"))
  except:
    errors.append({
      "field": "Inventario",
      "message": "El inventario debe ser un número"
    })
    
  code_found = session.query(Parts).filter_by(code = part.get("code")).first()
  
  brand = session.query(Brands).filter_by(name = part.get("brand")).first()
  category = session.query(Categories).filter_by(name = part.get("category")).first()
  
  if code_found:
    errors.append({ 
      "field": "Código", 
      "message": "El código ya existe" 
    })
    
  if not brand:
    errors.append({ 
      "field": "Marca", 
      "message": "La marca no existe" 
    })
    
  if not category:
    errors.append({ 
      "field": "Categoría", 
      "message": "La categoría no existe" 
    })
  
  return errors, brand, category