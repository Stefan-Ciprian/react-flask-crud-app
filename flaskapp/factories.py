import factory
from flaskapp.models import Category, Item
from flaskapp.database import db_session


class CategoryFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Category
        sqlalchemy_session = db_session
        sqlalchemy_session_persistence = "commit"

    category_name = factory.Faker("category_name")


class ItemFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Item
        sqlalchemy_session = db_session
        sqlalchemy_session_persistence = "commit"

    item_name = factory.Faker("item_name")
    category_id = factory.Faker("category_id")
