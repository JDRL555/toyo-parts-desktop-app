from models.User import Roles
from utils.database import session

def get_roles():
  roles = session.query(Roles).all()
  list_roles = [
    { 
      "id": role.id, 
      "name": role.name 
    } for role in roles
  ]
  return list_roles

def create_role(data):
  if not data.get("name"):
    return {
      "message": "Informacion invalida. Se espera un name"
    }, 400
  
  new_role = Roles(data.get("name"))
  
  try:
    session.add(new_role)
    session.commit()    
    return {
      "message": "Rol creado exitosamente!"
    }, 201
  except:
    return {
      "message": "El rol ya existe"
    }, 400
    
def update_role(role_id, new_data):
  role = {}
  
  role = session.query(Roles).get(role_id)
  
  if not role:
    return {
      "message": "Role no encontrado"
    }, 404
  
  if new_data.get("name"): role.name = new_data.get("name")  

  session.commit()
  
  return {
    "message": "Role actualizado"
  }
  
def delete_role(role_id):
  role = session.query(Roles).get(role_id)
  
  if not role:
    return {
      "message": "Role no encontrado"
    }, 404
  
  session.delete(role)
  session.commit()
  
  return {}, 204