
from models.Part import Categories
from utils.database import session

def get_categories():
  categories = session.query(Categories).all()
  list_categories = [
    { 
      "id": categorie.id, 
      "name": categorie.name 
    } for categorie in categories
  ]
  return list_categories

def create_category(data):
  if not data.get("name"):
    return {
      "message": "Informacion invalida. Se espera un name"
    }, 400
  
  new_categorie = Categories(data.get("name"))
  
  try:
    session.add(new_categorie)
    session.commit()    
    return {
      "message": "Categoria creada exitosamente!"
    }, 201
  except:
    return {
      "message": "La categoria ya existe"
    }, 400
    
def update_category(category_id, new_data):
  categorie = {}
  
  categorie = session.query(Categories).get(category_id)
  
  if not categorie:
    return {
      "message": "Categoria no encontrada"
    }, 404
  
  if new_data.get("name"): categorie.name = new_data.get("name")  

  session.commit()
  
  return {
    "message": "Categoria actualizada"
  }
  
def delete_category(category_id):
  categorie = session.query(Categories).get(category_id)
  
  if not categorie:
    return {
      "message": "Categoria no encontrada"
    }, 404
  
  session.delete(categorie)
  session.commit()
  
  return {}, 204