import sqlite3


class DB:
    def __init__(self):
        self.conn = self.get_db_connection()

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_db_connection(self):
        conn = sqlite3.connect('database.db')
        conn.row_factory = self.dict_factory

        return conn

    def get_categories(self):
        cursor = self.conn.cursor()
        categories = cursor.execute('SELECT * FROM category').fetchall()

        return {
            'categories': categories
        }

    def get_items(self, category_id):
        cursor = self.conn.cursor()
        items = cursor.execute('SELECT * FROM item WHERE category_id = ?', category_id).fetchall()

        self.conn.close()

        return {
            'items': items
        }

    def insert_item(self):
        self.conn.execute('INSERT INTO item (category_id, item_name) VALUES (?, ?)', (category_id, item_name))
        self.conn.commit()

        return {
            'status': True
        }

    def edit_item(self):
        self.conn.execute('UPDATE item SET item_name = ? WHERE id = ?', (new_item_name, item_id))
        self.conn.commit()

        return {
            'status': True
        }

    def delete_item(self):
        self.conn.execute('DELETE FROM item WHERE id = ?', (item_id,))
        self.conn.commit()

        return {
            'status': True
        }

    def __del__(self):
        self.conn.close()
