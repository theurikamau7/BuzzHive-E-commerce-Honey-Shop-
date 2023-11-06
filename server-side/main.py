import argparse
import http.server
import socketserver
import json
import bcrypt
from database import initialize_database, create_user, find_user_by_email, get_all_honey_types, create_order

# Create a new argparse parser
parser = argparse.ArgumentParser(description="Manage honey types")

# Subparsers for different commands
subparsers = parser.add_subparsers(dest="command")

# Command to add a honey type
add_parser = subparsers.add_parser("add", help="Add a honey type")
add_parser.add_argument("name", type=str, help="Name of the honey type")
add_parser.add_argument("description", type=str, help="Description of the honey type")
add_parser.add_argument("rate", type=float, help="Rate of the honey type")
add_parser.add_argument("amount", type=int, help="Amount of the honey type")
add_parser.add_argument("image_url", type=str, help="Image URL of the honey type")

# Command to list all honey types
list_parser = subparsers.add_parser("list", help="List all honey types")

# Command to search for a honey type
search_parser = subparsers.add_parser("search", help="Search for a honey type")
search_parser.add_argument("name", type=str, help="Name of the honey type to search")

# Command to create an order
order_parser = subparsers.add_parser("order", help="Create a new order")
order_parser.add_argument("user_id", type=int, help="User ID for the order")
order_parser.add_argument("honey_type_id", type=int, help="Honey Type ID for the order")
order_parser.add_argument("quantity", type=int, help="Quantity of honey to order")

# Initialize the database
initialize_database()

# API Endpoint for retrieving honey data
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

    def do_GET(self):
        if self.path == '/honey-types':
            honey_types = get_all_honey_types()
            honey_type_data = [
                {"name": honey[1], "description": honey[2], "rate": honey[3], "amount": honey[4], "image_url": honey[5]}
                for honey in honey_types
            ]

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(honey_type_data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(body)

        if self.path == '/signup':
            username = data['username']
            email = data['email']
            password = data['password']

            existing_user = find_user_by_email(email)
            if existing_user:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"message": "User with this email already exists"}).encode('utf-8'))
                return



            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            create_user(username, email, hashed_password)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "User registered successfully"}).encode('utf-8'))

        elif self.path == '/order':
            user_id = data['user_id']
            honey_type_id = data['honey_type_id']
            quantity = data['quantity']
            create_order(user_id, honey_type_id, quantity)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Order created successfully"}).encode('utf-8'))

        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    args = parser.parse_args()

    if args.command == "add":
        # Retrieve arguments
        name = args.name
        description = args.description
        rate = args.rate
        amount = args.amount
        image_url = args.image_url

        # Implement the logic to add a honey type with image_url
        print(f"Adding a honey type: {name}, Description: {description}, Rate: {rate}, Amount: {amount}, Image URL: {image_url}")

    elif args.command == "list":
        honey_types = get_all_honey_types()
        honey_type_data = [
            {"name": honey[1], "description": honey[2], "rate": honey[3], "amount": honey[4], "image_url": honey[5]}
            for honey in honey_types
        ]

        print("Listing all honey types")
        print(honey_type_data)

    elif args.command == "search":
        name = args.name
        print(f"Searching for honey type: {name}")

    with socketserver.TCPServer(("", 80), CustomHandler) as httpd:
        print("Serving at port 80")
        httpd.serve_forever()