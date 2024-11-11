from utils.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func

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
    
class PaymentHistory(Base):
  __tablename__ = "payment_history"
  
  id = Column(Integer, primary_key=True)
  part_id = Column(Integer, ForeignKey('parts.id'), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  paid_at = Column(DateTime(timezone=True), server_default=func.now())
  
  def __init__(self, part_id, user_id):
    self.part_id = part_id
    self.user_id = user_id