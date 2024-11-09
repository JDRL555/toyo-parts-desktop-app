from controllers import parts as part_controller
from controllers import payments as payment_controller

class Controller:
  def get(self, page = 1, is_admin = False): 
    return part_controller.get_parts(page=page, is_admin=is_admin)
  
  def get_len(self, is_admin = False):
    return part_controller.get_parts_len(is_admin=is_admin)
  
  def buy(self, part_id, user_id):
    data = {
      "part_id": part_id,
      "user_id": user_id,
    }
    return payment_controller.register_payment(data=data)
  
  def delete(self, id):
    return part_controller.delete_part(id=id)