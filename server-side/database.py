import sqlite3

def initialize_database():
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS honey_types (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            image_url TEXT NOT NULL,
            description TEXT NOT NULL,
            rate REAL NOT NULL,
            amount REAL NOT NULL
        )
    ''')

    # Insert hardcoded honey types (your existing data)
    honey_types_data = [
        ("Clover Honey", "https://biene-theme.myshopify.com/cdn/shop/products/p14_720x.jpg?v=1597915976", "A classic, sweet honey with a mild floral taste.", 4.5, 250),
        ("Wildflower Honey", "https://biene-theme.myshopify.com/cdn/shop/products/p15-ns_dbb339b5-731b-4d60-b7f3-ad9025cba68d_720x.jpg?v=1601974254", "A rich, amber-colored honey with a variety of floral flavors.", 4.2, 300),
        ("Manuka Honey", "https://biene-theme.myshopify.com/cdn/shop/products/p12-ns_66d85889-776c-4791-b4d2-addfafe941ea_720x.jpg?v=1601974253", "Renowned for its potential health benefits and unique flavor.", 4.8, 200),
        ("Acacia Honey", "https://beeswax-theme.myshopify.com/cdn/shop/products/shop-04_ffa34f8d-5c28-444c-8ca0-f346167b7d74_600x.png?v=1643975020", "Delicate and light, known for its mild and subtle taste.", 4.7, 350),
        ("Orange Blossom Honey", "https://beeswax-theme.myshopify.com/cdn/shop/products/shop-04_5eaa9871-4e1f-40ac-8ec4-1fb1ff459abf_600x.png?v=1643975001", "Sweet and citrusy, with a hint of orange blossom aroma.", 4.3, 275),
        ("Lavender Honey", "https://beeswax-theme.myshopify.com/cdn/shop/products/shop-04_600x.png?v=1643974438", "Delightfully fragrant with a distinct lavender note.", 4.6, 225),
        ("Eucalyptus Honey", "https://beeswax-theme.myshopify.com/cdn/shop/products/shop-03_05ee16c9-48fd-4264-8244-07b54c0c62c3_600x.png?v=1643975036", "Robust and slightly medicinal, derived from eucalyptus trees.", 4.1, 320),
        ("Buckwheat Honey", "https://beeswax-theme.myshopify.com/cdn/shop/products/shop-04_7fda1a5a-a6e8-40b7-9f41-5a7513e782a3_600x.png?v=1643974893", "Dark and bold, offering a strong molasses-like flavor.", 4.0, 275),
        ("Blueberry Honey", "https://biene-theme.myshopify.com/cdn/shop/products/p15-ns_720x.jpg?v=1601973329", "Infused with the essence of blueberries, a sweet treat.", 4.4, 240),
        ("Sage Honey", "https://beeswax-theme.myshopify.com/cdn/shop/products/shop-04_5eaa9871-4e1f-40ac-8ec4-1fb1ff459abf_600x.png?v=1643975001", "Herbaceous and earthy, known for its unique and strong taste.", 4.9, 280)
    ]

    cursor.executemany("INSERT INTO honey_types (name, image_url, description, rate, amount) VALUES (?, ?, ?, ?, ?)", honey_types_data)

    connection.commit()
    connection.close()

# Create a new User
def create_user(username, email, password):
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    connection.commit()
    connection.close()

# Find a user by email and return user data as a dictionary
def find_user_by_email(email):
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user_data = cursor.fetchone()
    connection.close()

    if user_data:
        user = {
            'id': user_data[0],
            'username': user_data[1],
            'email': user_data[2],
            'password': user_data[3]
        }
        return user
    else:
        return None

# Get all honey types
def get_all_honey_types():
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM honey_types")
    honey_types = cursor.fetchall()
    connection.close()
    return honey_types