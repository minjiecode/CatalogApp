from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

# Record User information
class User(Base):
    __tablename__ = 'user'

    name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
    picture = Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)


# Set up different categories
class Category(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    # user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id
       }

# Record App name and details 
class App(Base):
    __tablename__ = 'app'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    developer = Column(String(80), nullable = False)
    description = Column(String(500))
    price = Column(String(80))
    website = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship("Category", 
      backref="App")
    # ,cascade = "all, delete-orphan"
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'app name'         : self.name,
           'description'         : self.description,
           'APP ID'         : self.id,
           'developer'         : self.developer,
           'website'         : self.website,
           'category id'         : self.category_id,
           'creator id'         : self.user_id,
           'price'            : self.price
       }



engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
 

Base.metadata.create_all(engine)
