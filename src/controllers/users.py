from bcrypt import hashpw, gensalt

from utils.validate import is_email_valid
from utils.database import session
from models.User import Users, Roles

def get_users():
  users = session.query(Users).all()
  list_users = []
  
  for user in users:
    role = session.query(Roles).get(user.role_id)

    list_users.append({
      "id": user.id,
      "fullname": user.fullname,
      "email": user.email,
      "role": {
        "id": role.id,
        "name": role.name
      }
    })
    
  return list_users

def create_user(data):
  role = {}
  if not data.get("fullname") or not data.get("email") or not data.get("password"):
    return {
      "message": "Informacion invalida. Se espera fullname, email y password"
    }, 400
    
  if not is_email_valid(data.get("email")):
    return {
      "message": "El correo es invalido"
    }, 400
  
  hashed_password = hashpw(data.get("password").encode("utf-8"), gensalt(12))
  
  if data.get("role"):
    role = session.query(Roles).filter_by(name=data.get("role")).first()
    
    if not role:
      return {
        "message": "Role no encontrado"
      }, 404
      
  role_client = session.query(Roles).filter_by(name="cliente").first()
  
  new_user = {
    "fullname": data.get("fullname"),
    "email": data.get("email"),
    "password": hashed_password,
    "role_id": role_client.id if not role else role.id
  }
  
  user = Users(**new_user)
  
  try:
    session.add(user)
    session.commit()
    
    return {
      "message": "User creado exitosamente!"
    }, 201
    
  except Exception:
    return {
      "message": f"El usuario con correo {user.email} ya existe"
    }, 400
    
def update_user(user_id, new_data):
  role = {}
  
  user = session.query(Users).get(user_id)
  
  if not user:
    return {
      "message": "Usuario no encontrado"
    }, 404
  
  if new_data.get("fullname"): user.fullname = new_data.get("fullname")  
  if new_data.get("email"): 
    if not is_email_valid(new_data.get("email")):
      return {
        "message": "Email no valido"
      }, 400
    user.email = new_data.get("email")
  if new_data.get("role"):
    role = session.query(Roles).filter_by(name=new_data.get("role")).first()
    
    if not role:
      return {
        "message": "Role no encontrado"
      }, 404
      
    user.role_id = role.id
    
  session.commit()
  
  return {
    "message": "Usuario actualizado"
  }
  
def delete_user(user_id):
  user = session.query(Users).get(user_id)
  
  if not user:
    return {
      "message": "Usuario no encontrado"
    }, 404
  
  session.delete(user)
  session.commit()
  
  return {}, 204