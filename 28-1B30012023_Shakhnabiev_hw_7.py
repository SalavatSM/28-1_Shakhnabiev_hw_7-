import sqlite3

# connection func
def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

# table creation func
def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

# product creation func
def create_product(connection, products):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

# product selection func
def select_all_products(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

# product price update func
def update_products_price(connection, products):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

# product quantity update func
def update_products_quantity(connection, products):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

# product delete func
def delete_products(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

# product selection by price and quantity func
def select_products_by_price_and_quantity(connection, price_limit, quantity_limit):
    try:
        sql = '''SELECT * FROM products WHERE price >= ? and quantity >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

# product find by word func
def find_products_by_word(connection, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (word,))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

data_base_name = 'hw.db'

sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0)
'''

connection_to_db = create_connection(data_base_name)
if connection_to_db is not None:
    print('Successfully connected!')

    # create_table(connection_to_db, sql_create_products_table)
    # create_product(connection_to_db, ('water', 60.00, 100))
    # create_product(connection_to_db, ('water', 500.00, 500))
    # create_product(connection_to_db, ('water', 60.00, 100))
    # create_product(connection_to_db, ('milk', 70.00, 50))
    # create_product(connection_to_db, ('bread', 30.00, 60))
    # create_product(connection_to_db, ('butter', 110.00, 30))
    # create_product(connection_to_db, ('tomato', 65.00, 70))
    # create_product(connection_to_db, ('apple', 55.00, 80))
    # create_product(connection_to_db, ('fish', 600.00, 40))
    # create_product(connection_to_db, ('meat', 550.00, 55))
    # create_product(connection_to_db, ('rice', 75.00, 100))
    # create_product(connection_to_db, ('cheese', 250.00, 35))
    # create_product(connection_to_db, ('cucumber', 62.00, 68))
    # create_product(connection_to_db, ('carrot', 32.00, 100))
    # create_product(connection_to_db, ('banana', 58.00, 80))
    # create_product(connection_to_db, ('chocolate', 210.00, 79))
    # create_product(connection_to_db, ('egg', 70.00, 79))
    #create_product(connection_to_db, ('milk chocolate', 230.00, 95))

    # select_all_products(connection_to_db)

    # select_products_by_price_and_quantity(connection_to_db, 60, 65)

    # changed rise price from 75 to 85
    # update_products_price(connection_to_db, (85, 11))

    # changed water quantity 100 ->150
    # update_products_quantity(connection_to_db, (150, 1))

    # deleted water duplication
    # delete_products(connection_to_db, 18)

    # find product by word # output: milk, milk chocolate
    #find_products_by_word(connection_to_db, '%milk%')

    connection_to_db.close()
    print('DONE!')
else:
    print('Connection failed')

