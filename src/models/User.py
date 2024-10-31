from utils.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Roles(Base):
  __tablename__ = "roles"
  
  id = Column(Integer, primary_key=True)
  name = Column(String(100), unique=True)
  
  def __init__(self, name):
    self.name = name

class Users(Base):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True)
  fullname = Column(String(100))
  email = Column(String(100), unique=True)
  password = Column(String(500))
  role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
  
  def __init__(self, fullname, email, password, role_id):
    self.fullname = fullname
    self.email = email
    self.password = password
    self.role_id = role_id