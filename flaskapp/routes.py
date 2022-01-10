from flask import Blueprint, request
from flaskapp.models import Category, Item
from flaskapp.db import db

items = Blueprint('items', __name__)


@items.route('/')
def index():
    return items.send_static_file('index.html')


@items.route('/get_categories', methods=['GET'])
def get_categories():
    categories = [row2dict(item) for item in db.session.query(Category).all()]

    return {
        'categories': categories
    }


@items.route('/get_items/<category_id>', methods=['GET'])
def get_items(category_id):
    category_items = [row2dict(item) for item in db.session.query(Item).filter_by(category_id=category_id).all()]

    return {
        'items': category_items
    }


@items.route('/insert_item', methods=['POST'])
def insert_item():
    category_id = request.json.get('category_id')
    item_name = request.json.get('item_name')

    item = Item(category_id=category_id, item_name=item_name)
    db.session.add(item)
    db.session.commit()

    return {
        'status': True
    }


@items.route('/edit_item', methods=['POST'])
def edit_item():
    item_id = request.json.get('item_id')
    new_item_name = request.json.get('new_item_name')

    item = Item.query.filter_by(id=item_id).first()
    item.item_name = new_item_name
    db.session.commit()

    return {
        'status': True
    }


@items.route('/delete_item', methods=['POST'])
def delete_item():
    item_id = request.json.get('item_id')

    item = Item.query.filter_by(id=item_id).first()
    db.session.delete(item)
    db.session.commit()

    return {
        'status': True
    }


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d
