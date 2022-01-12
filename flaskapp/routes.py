from flask import Blueprint, request
from flaskapp.database import db_session
from flaskapp.models import Category, Item


items = Blueprint('items', __name__)


@items.route('/')
def index():
    return items.send_static_file('index.html')


@items.route('/get_categories', methods=['GET'])
def get_categories():
    categories = [item.serialize for item in Category.query.all()]

    return {
        'categories': categories
    }


@items.route('/get_items/<category_id>', methods=['GET'])
def get_items(category_id):
    category_items = [item.serialize for item in Item.query.filter(Item.category_id == category_id).all()]

    return {
        'items': category_items
    }


@items.route('/insert_item', methods=['POST'])
def insert_item():
    category_id = request.json.get('category_id')
    item_name = request.json.get('item_name')

    item = Item(item_name=item_name, category_id=category_id)
    db_session.add(item)
    db_session.commit()

    return {
        'status': True
    }


@items.route('/edit_item', methods=['POST'])
def edit_item():
    item_id = request.json.get('item_id')
    new_item_name = request.json.get('new_item_name')

    item = Item.query.filter(Item.id == item_id).first()
    item.item_name = new_item_name
    db_session.commit()

    return {
        'status': True
    }


@items.route('/delete_item', methods=['POST'])
def delete_item():
    item_id = request.json.get('item_id')

    item = Item.query.filter(Item.id == item_id).first()
    db_session.delete(item)
    db_session.commit()

    return {
        'status': True
    }
