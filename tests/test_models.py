from flaskapp.models import Category, Item
from flaskapp.factories import CategoryFactory, ItemFactory


def test_insert_categories_with_items(session):
    categories = session.query(Category).all()
    items = session.query(Item).all()
    assert len(categories) == 0
    assert len(items) == 0

    category_one = CategoryFactory(category_name="Laptops")
    category_two = CategoryFactory(category_name="Phones")

    ItemFactory(item_name="MacBook Pro", category_id=category_one.id)
    ItemFactory(item_name="MacBook", category_id=category_one.id)
    ItemFactory(item_name="iPhone 13", category_id=category_two.id)

    categories = session.query(Category).all()
    items = session.query(Item).all()
    assert len(categories) == 2
    assert len(items) == 3


def test_edit_category(session):
    category = session.query(Category).filter_by(category_name="Laptops").first()
    category.category_name = "New laptops"
    session.add(category)
    session.commit()

    assert session.query(Category).filter_by(category_name="New laptops").one_or_none()


def test_edit_item(session):
    item = session.query(Item).filter_by(item_name="MacBook Pro").first()
    item.item_name = "New MacBook Pro"
    session.add(item)
    session.commit()

    assert session.query(Item).filter_by(item_name="New MacBook Pro").one_or_none()


def test_delete_category_with_items(session):
    category = session.query(Category).filter_by(category_name="New laptops").first()

    items = session.query(Item).filter_by(category_id=1).all()

    for item in items:
        session.delete(item)
        session.commit()

    session.delete(category)
    session.commit()

    categories = session.query(Category).all()
    items = session.query(Item).all()
    assert len(categories) == 1
    assert len(items) == 1

