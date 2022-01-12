from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flaskapp.database import Base


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    category_name = Column(String(100))

    def __repr__(self):
        return f'<Category {self.category_name!r}>'

    @property
    def serialize(self):
        return {
            'id': self.id,
            'category_name': self.category_name,
        }


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    item_name = Column(String(100))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    def __repr__(self):
        return f'<Item {self.item_name!r}>'

    @property
    def serialize(self):
        return {
            'id': self.id,
            'item_name': self.item_name,
            'category_id': self.category_id
        }
