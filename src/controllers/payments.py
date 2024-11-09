from models.Part import Parts, PaymentHistory
from models.User import Users

from utils.database import session

def get_payments_len(is_admin = False):
  payments_query = session.query(PaymentHistory)
  result = payments_query.all() if is_admin else payments_query.filter(PaymentHistory.quantity != 0).all()
  return len(result)

def get_payments(page = 1, is_admin = False):
  global payments
  per_page = 29
  list_payments = []
  
  try:
    payments_query = session.query(PaymentHistory)
    result = payments_query if is_admin else payments_query.filter(PaymentHistory.quantity != 0)
    payments = result.offset((page - 1) * per_page).limit(per_page).all()
  except Exception as err:
    print(err)
    return []
  
  if len(payments) == 0:
    return []
  
  for payment in payments:
    part = session.query(Parts).get(payment.part_id)
    user = session.query(Users).get(payment.user_id)

    list_payments.append({
      "id": payment.id,
      "part": {
        "id": part.id,
        "code": part.code,
        "quantity": part.quantity,
        "description": part.description,
        "cost": part.cost,
        "price": part.price,
        "inventory": part.inventory
      },
      "user": {
        "id": user.id,
        "fullname": user.fullname,
        "email": user.email,
      },
      "paid_at": payment.paid_at,
    })
    
  return list_payments

def register_payment(data):
  expected_fields = ["part_id", "user_id"]
  
  for key in data.keys():
    if key not in expected_fields:
      return {
        "message": "Informacion invalida"
      }, 400
      
  part = session.query(Parts).get(data.get("part_id"))
  user = session.query(Users).get(data.get("user_id"))
  
  if not part:
    return {
        "message": "Parte no encontrada"
      }, 404
    
  if not user:
    return {
        "message": "Usuario no encontrado"
      }, 404
  
  payment = {
    "part_id": part.id,
    "user_id": user.id
  }
  
  new_payment = PaymentHistory(**payment)
  
  session.add(new_payment)
  session.commit()
  
  return {
    "message": "Pago registrado exitosamente!"
  }, 201