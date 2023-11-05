import http.server
import socketserver
import json
import bcrypt
from database import initialize_database, create_user, get_all_honey_types, find_user_by_email
from models import User, HoneyType

PORT = 80

# Initialize the database
initialize_database()

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(body)

        if self.path == '/signup':
            username = data['username']
            email = data['email']
            password = data['password']

            # Check if the user already exists
            existing_user = find_user_by_email(email)
            if existing_user:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"message": "User with this email already exists"}).encode('utf-8'))
                return

            # Hash the password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            # Create a user in the database
            create_user(username, email, hashed_password)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "User registered successfully"}).encode('utf-8'))

        elif self.path == '/login':
            email = data['email']
            password = data['password']

            # Fetch the user from the database by email
            user = find_user_by_email(email)
            if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"message": "Login successful"}).encode('utf-8'))
            else:
                self.send_response(401)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"message": "Login failed"}).encode('utf-8'))

        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if self.path == '/honey-types':
            honey_types = get_all_honey_types()
            honey_type_data = [{"name": honey[1], "image_url": honey[2], "description": honey[3], "rate": honey[4], "amount": honey[5]} for honey in honey_types]

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(honey_type_data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()