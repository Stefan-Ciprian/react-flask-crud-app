import os
from flask import Flask, request
import sqlite3


app = Flask(__name__, static_folder='build/', static_url_path='/')
app.debug = 'DEBUG' in os.environ


@app.route('/')
def index():
    return app.send_static_file('index.html')


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_db_connection():
    conn = sqlite3.connect('db_handler/database.db')
    conn.row_factory = dict_factory
    return conn


@app.route('/get_categories', methods=['GET'])
def get_categories():
    conn = get_db_connection()
    cursor = conn.cursor()
    categories = cursor.execute('SELECT * FROM category').fetchall()

    conn.close()

    return {
        'categories': categories
    }


@app.route('/get_items/<category_id>', methods=['GET'])
def get_items(category_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    items = cursor.execute('SELECT * FROM item WHERE category_id = ?', category_id).fetchall()

    conn.close()

    return {
        'items': items
    }


@app.route('/insert_item', methods=['POST'])
def insert_item():
    category_id = request.json.get('category_id')
    item_name = request.json.get('item_name')

    conn = get_db_connection()
    conn.execute('INSERT INTO item (category_id, item_name) VALUES (?, ?)', (category_id, item_name))
    conn.commit()
    conn.close()

    return {
        'status': True
    }


@app.route('/edit_item', methods=['POST'])
def edit_item():
    item_id = request.json.get('item_id')
    new_item_name = request.json.get('new_item_name')

    conn = get_db_connection()
    conn.execute('UPDATE item SET item_name = ? WHERE id = ?', (new_item_name, item_id))
    conn.commit()
    conn.close()

    return {
        'status': True
    }


@app.route('/delete_item', methods=['POST'])
def delete_item():
    item_id = request.json.get('item_id')

    conn = get_db_connection()
    conn.execute('DELETE FROM item WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()

    return {
        'status': True
    }


