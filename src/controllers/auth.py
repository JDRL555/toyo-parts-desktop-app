from bcrypt import checkpw
from models.User import Users, Roles

from utils.database import session

def login(email, password):
  user = session.query(Users).filter_by(email=email).first()
  
  if not user:
    return {
      "message": "Correo incorrecto o el usuario no existe"
    }, 404
    
  if not checkpw(password=password.encode("utf-8"), hashed_password=user.password.encode("utf-8")):
    return {
      "message": "Clave incorrecta"
    }, 401
    
  role = session.query(Roles).get(user.role_id)
  return {
      "message": "Sesion iniciada correctamente!",
      "user": {
        "id": user.id,
        "fullname": user.fullname,
        "email": user.email,
        "role": role.name,
      }
    }, 200