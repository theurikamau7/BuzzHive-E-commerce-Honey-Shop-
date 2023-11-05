# models.py remains the same
class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

class HoneyType:
    def __init__(self, id, name, image_url, description, rate, amount):
        self.id = id
        self.name = name
        self.image_url = image_url
        self.description = description
        self.rate = rate
        self.amount = amount