from models.Part import Parts, Categories, Brands
from utils.database import session

def get_parts_len():
  return len(session.query(Parts).all())

def get_parts(page = 1):
  global parts
  per_page = 29
  list_parts = []
  
  try:
    parts = session.query(Parts).offset((page - 1) * per_page).limit(per_page).all()
  except Exception as err:
    print(err)
    return []
  
  if len(parts) == 0:
    return []
  
  for part in parts:
    brand = session.query(Brands).get(part.brand_id)
    category = session.query(Categories).get(part.category_id)

    list_parts.append({
      "id": part.id,
      "code": part.code,
      "quantity": part.quantity,
      "description": part.description,
      "cost": part.cost,
      "price": part.price,
      "inventory": part.inventory,
      "brand": {
        "id": brand.id,
        "name": brand.name,
      },
      "category": {
        "id": category.id,
        "name": category.name,
      },
    })
    
  return list_parts

def create_part(data):
  expected_fields = ["code", "description", "quantity", "brand_id", "category_id", "cost", "price", "inventory"]
  
  for key in data.keys():
    if key not in expected_fields:
      return {
        "message": "Informacion invalida"
      }, 400
      
  brand = session.query(Brands).get(data.get("brand_id"))
  category = session.query(Categories).get(data.get("category_id"))
  
  if not brand:
    return {
        "message": "Marca no encontrada"
      }, 404
    
  if not category:
    return {
        "message": "Categoria no encontrada"
      }, 404
  
  part = {
    "code": data.get("code"),
    "description": data.get("description"),
    "quantity": data.get("quantity"),
    "brand_id": data.get("brand_id"),
    "category_id": data.get("category_id"),
    "cost": data.get("cost"),
    "price": data.get("price"),
    "inventory": data.get("inventory"),
  }
  
  new_part = Parts(**part)
  
  session.add(new_part)
  session.commit()
  
  return {
    "message": "Parte creada exitosamente!"
  }, 201
  
def edit_part(id, new_data):
  part = session.query(Parts).get(id)
  
  if not part:
    return {
      "message": "Parte no encontrada"
    }, 404
    
  if new_data.get("code"): part.code = new_data.get("code")
  if new_data.get("description"): part.description = new_data.get("description")
  
  if new_data.get("quantity"): 
    try:
      part.quantity = int(new_data.get("quantity"))
    except:
      return {
        "message": "La cantidad debe ser un numero valido"
      }
      
  if new_data.get("cost"): 
    try:
      part.cost = float(new_data.get("cost"))
    except:
      return {
        "message": "El costo debe ser un numero valido"
      }
      
    
  if new_data.get("price"): 
    try:
      part.price = float(new_data.get("price"))
    except:
      return {
        "message": "El precio debe ser un numero valido"
      }
      
    
  if new_data.get("inventory"): 
    try:
      part.inventory = float(new_data.get("inventory"))
    except:
      return {
        "message": "El inventario debe ser un numero valido"
      }
      
  if new_data.get("brand_id"):
    brand = session.query(Brands).get(new_data.get("brand_id"))
    
    if not brand:
      return {
        "message": "Marca no encontrada"
      }, 
      
    part.brand_id = new_data.get("brand_id")
      
  if new_data.get("category_id"):
    category = session.query(Categories).get(new_data.get("category_id"))
    
    if not category:
      return {
        "message": "Categoria no encontrada"
      }, 404
      
    part.category_id = new_data.get("category_id")
  
  session.commit()
  
  return {
    "message": "Parte actualizada"
  }, 200
  
def delete_part(id):
  part = session.query(Parts).get(id)
  
  if not part:
    return {
      "message": "Parte no encontrada"
    }, 404
    
  session.delete(part)
  session.commit()
  
  return {
    "message": "Parte eliminada"
  }, 200