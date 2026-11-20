from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    sku = Column(String, unique=True, index=True, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")
    
    inventory = relationship("Inventory", back_populates="product", uselist=False)

class Inventory(Base):
    __tablename__ = "inventories"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), unique=True)
    quantity = Column(Integer, default=0)
    min_stock = Column(Integer, default=10)
    max_stock = Column(Integer, default=300)


    product = relationship("Product", back_populates="inventory")

class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key= True, index = True)
    first_name= Column(String, nullable= False)
    last_name= Column(String, nullable= False)
    email = Column(String, unique= True, index = True, nullable = False)
    phone= Column(String, unique= True, index= True, nullable = False)
    password = Column(String, nullable= False)

    type = Column( String(50))

    __maper_args__={'polymorphic_identity':'user',
                    'polymorphic_on': type}

class Client(User):
    __tablename__='clients'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    shipping_address= Column(String, nullable  = True)

    __maper_args__ = {'polymorphic_identity': 'client'}

class Seller(User):
    __tablename__= 'sellers'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    store_name = Column(String, nullable = False)
    store_logo = Column(String, nullable = True)

    __maper_args__ = {'polymorphic_identity' : 'seller'}

class Admin(User):
    __tablename__ = "admins"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    permissions_level = Column(Integer, default=1)

    __mapper_args__ = {"polymorphic_identity": "admin"}