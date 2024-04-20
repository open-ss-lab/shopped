from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from api.db.conn import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    role = Column(String, default="user")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    image_publi_id = Column(String)

    products = relationship("Product", back_populates="category")
    banners = relationship("Banner", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    image = Column(String)
    image_public_id = Column(String)
    is_offer = Column(Boolean)
    offer_price = Column(Integer)
    punctuation = Column(Integer)
    quantity = Column(Integer)
    description = Column(String, index=True)
    brand = Column(String)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")


class Banner(Base):
    __tablename__ = "banners"

    id = Column(Integer, primary_key=True)
    title = Column(String(10))
    description = Column(String(30))

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="banners")
