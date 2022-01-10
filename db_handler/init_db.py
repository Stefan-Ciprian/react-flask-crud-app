import sqlite3

connection = sqlite3.connect('db_handler/database.db')


with open('db_handler/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO category (`category_name`) VALUES ('Laptops')")
cur.execute("INSERT INTO category (`category_name`) VALUES ('Phones')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (1,'Dell Inspiron 15 3000')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (1,'Dell Inspiron 14')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (1,'Dell New Inspiron 15')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (1,'Dell XPS 13 9305')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (1,'MacBook Air')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (1,'MacBook Pro')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (2,'iPhone 13')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (2,'iPhone 13 Mini')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (2,'iPhone 13 Pro')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (2,'iPhone 13 Pro Max')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (2,'Samsung Galaxy Z Flip3 5G')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (2,'Samsung Galaxy Z Fold3')")
cur.execute("INSERT INTO item (category_id, item_name) VALUES (2,'Samsung Galaxy S21')")

connection.commit()
connection.close()
