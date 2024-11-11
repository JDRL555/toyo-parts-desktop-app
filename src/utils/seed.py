from bcrypt import hashpw, gensalt
from models.Part import Categories, Brands, Parts
from models.User import Roles, Users
from data.categories import categories
from data.brands import brands
import json
import os

json_file = open(os.path.join(os.path.curdir, "src/data/parts.json"), "r")
parts_list = json.load(json_file)

def seed(session):
  
  if len(session.query(Roles).all()) == 0:
    client = Roles(name="cliente")
    admin = Roles(name="administrador")
    
    session.add(client)
    session.commit()
    session.add(admin)
    session.commit()
    
  if len(session.query(Users).all()) == 0:
    role_client = session.query(Roles).filter_by(name="cliente").first()
    role_admin = session.query(Roles).filter_by(name="administrador").first()
    
    user_client = Users(
      fullname="Jose Gonzales", 
      email="jose@gmail.com", 
      password=hashpw(b"jose123", gensalt()), 
      role_id=role_client.id
    )
    
    user_admin = Users(
      fullname="Juan Perez", 
      email="juan@gmail.com", 
      password=hashpw(b"juan123", gensalt()),
      role_id=role_admin.id
    )
    
    session.add(user_client)
    session.commit()
    session.add(user_admin)
    session.commit()
  
  if len(session.query(Categories).all()) == 0:
    for category in categories:
      new_category = Categories(category)
      session.add(new_category)
      session.commit()
      
  if len(session.query(Brands).all()) == 0:
    for brand in brands:
      new_brand = Brands(brand)
      session.add(new_brand)
      session.commit()
    
  if len(session.query(Parts).all()) == 0:
    for part in parts_list:
      brand = session.query(Brands).filter_by(name=part["brand"]).first()
      category = session.query(Categories).filter_by(name=part["category"]).first()
      
      part_dict = {
        "code": part["code"],
        "quantity": part["quantity"],
        "description": part["description"],
        "cost": part["cost"],
        "price": part["price"],
        "inventory": part["inventory"],
        "brand_id": brand.id,
        "category_id": category.id,
      }
      
      new_part = Parts(**part_dict)
      session.add(new_part)
      session.commit()