from utils.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Categories(Base):
  __tablename__ = "categories"
  
  id = Column(Integer, primary_key=True)
  name = Column(String(100))
  
  def __init__(self, name):
    self.name = name  
    
class Brands(Base):
  __tablename__ = "brands"

  id = Column(Integer, primary_key=True)
  name = Column(String(100))
  
  def __init__(self, name):
    self.name = name  
    
class Parts(Base):
  __tablename__ = "parts"
  
  id = Column(Integer, primary_key=True)
  code = Column(String(50))
  quantity = Column(Integer)
  description = Column(String(200))
  cost = Column(Float, nullable=True)
  price = Column(Float)
  inventory = Column(Float, nullable=True)
  brand_id = Column(Integer, ForeignKey('brands.id'), nullable=False)
  category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
  
  def __init__(self, code, quantity, description, cost, price, inventory, brand_id, category_id):
    self.code = code
    self.quantity = quantity
    self.description = description
    self.cost = cost
    self.price = price
    self.inventory = inventory
    self.brand_id = brand_id
    self.category_id = category_id