from models.Part import Brands
from utils.database import session

def get_brands():
  brands = session.query(Brands).all()
  list_brands = [
    { 
      "id": brand.id, 
      "name": brand.name 
    } for brand in brands
  ]
  return list_brands

def create_brand(data):
  if not data.get("name"):
    return {
      "message": "Informacion invalida. Se espera un name"
    }, 400
  
  new_brand = Brands(data.get("name"))
  
  try:
    session.add(new_brand)
    session.commit()    
    return {
      "message": "Marca creada exitosamente!"
    }, 201
  except:
    return {
      "message": "La marca ya existe"
    }, 400
    
def update_brand(brand_id, new_data):
  brand = {}
  
  brand = session.query(Brands).get(brand_id)
  
  if not brand:
    return {
      "message": "Marca no encontrada"
    }, 404
  
  if new_data.get("name"): brand.name = new_data.get("name")  

  session.commit()
  
  return {
    "message": "Marca actualizada"
  }
  
def delete_brand(brand_id):
  brand = session.query(Brands).get(brand_id)
  
  if not brand:
    return {
      "message": "Marca no encontrada"
    }, 404
  
  session.delete(brand)
  session.commit()
  
  return {}, 204