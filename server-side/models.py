import sqlite3

class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def find_user_by_email(cls, email):
        connection = sqlite3.connect('db.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user_data = cursor.fetchone()
        connection.close()

        if user_data:
            user = User(*user_data)
            return user
        else:
            return None

    # Other User methods here

class HoneyType:
    def __init__(self, id, name, image_url, description, rate, amount):
        self.id = id
        self.name = name
        self.image_url = image_url
        self.description = description
        self.rate = rate
        self.amount = amount

    @classmethod
    def get_all_honey_types(cls):
        connection = sqlite3.connect('db.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM honey_types")
        honey_types_data = cursor.fetchall()
        connection.close()

        honey_types = [HoneyType(*honey_data) for honey_data in honey_types_data]
        return honey_types

    # Other HoneyType methods here

class Order:
    def __init__(self, user_id, honey_type_id, quantity):
        self.user_id = user_id
        self.honey_type_id = honey_type_id
        self.quantity = quantity

    def save_to_database(self):
        connection = sqlite3.connect('db.sqlite')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO orders (user_id, honey_type_id, quantity) VALUES (?, ?, ?)",
                       (self.user_id, self.honey_type_id, self.quantity))
        connection.commit()
        connection.close()

    @classmethod
    def get_orders_by_user(cls, user_id):
        connection = sqlite3.connect('db.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        order_data = cursor.fetchall()
        connection.close()

        orders = [Order(*order) for order in order_data]
        return orders