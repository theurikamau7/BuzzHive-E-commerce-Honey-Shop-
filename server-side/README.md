# Honeybuzz Server Application

The Honey Server Application is a simple Python-based server for managing honey types and orders. This README provides an overview of how to use the Command-Line Interface (CLI) and describes the functions available in both `main.py` and `database.py`.

## Table of Contents

- [Getting Started](#getting-started)
- [CLI Commands](#cli-commands)
- [main.py Functions](#mainpy-functions)
- [database.py Functions](#databasepy-functions)

## Getting Started

Before running the Honey Server, make sure you have Python installed on your system. You can download and install Python from the [official Python website](https://www.python.org/downloads/).

To get started, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   cd HoneyServer
   ```

2. Initialize the database by running:

   ```bash
   python database.py
   ```

   This command creates the necessary SQLite database and initializes it with sample honey types.

3. Run the Honey Server:

   ```bash
   python main.py
   ```

   The server will start, and you'll be able to access it via a web browser or through the CLI.

## CLI Commands

The Honey Server Application provides a Command-Line Interface (CLI) for managing honey types and orders. The available commands are:

- **add:** Add a new honey type to the database.

  ```bash
  python main.py add "Honey Name" "Honey Description" 10.5 20 "https://example.com/honey.jpg"
  ```

- **list:** List all honey types in the database.

  ```bash
  python main.py list
  ```

- **search:** Search for a honey type by name.

  ```bash
  python main.py search "Honey Name"
  ```

- **order:** Create a new honey order.
  ```bash
  python main.py order user_id honey_type_id quantity
  ```
  You can use the CLI commands to perform various actions on honey types. Here's how to use each command:

1. **Add a Honey Type:**

   - To add a honey type, use the `add` command with the following syntax:
     ```
     python main.py add "Honey Name" "Honey Description" Rate Amount "Image URL"
     ```

   Replace `"Honey Name"`, `"Honey Description"`, `Rate`, `Amount`, and `"Image URL"` with the actual values you want to add.

2. **List All Honey Types:**

   - To list all honey types, use the `list` command:
     ```
     python main.py list
     ```

3. **Search for a Honey Type:**

   - To search for a honey type by name, use the `search` command:
     ```
     python main.py search "Honey Name"
     ```

   Replace `"Honey Name"` with the name of the honey type you want to search for.

4. **Create an Order:**

   - To create a new order, use the `order` command with the following syntax:
     ```
     python main.py order User_ID Honey_Type_ID Quantity
     ```

   Replace `User_ID`, `Honey_Type_ID`, and `Quantity` with the actual values for the order.

5. **Remove a Honey Type:**

   - To remove a honey type, use the `remove` command with the following syntax:
     ```
     python main.py remove Honey_Type_ID
     ```

   Replace `Honey_Type_ID` with the ID of the honey type you want to remove.

6. **Update a Honey Type:**

   - To update a honey type, use the `update` command with the following syntax:
     ```
     python main.py update Honey_Type_ID "New Honey Name" "New Honey Description" New_Rate New_Amount "New Image URL"
     ```

   Replace `Honey_Type_ID`, `"New Honey Name"`, `"New Honey Description"`, `New_Rate`, `New_Amount`, and `"New Image URL"` with the actual values for the update.

## main.py Functions

### `CustomHandler`

- `do_GET`: Handles GET requests for retrieving honey data.
- `do_POST`: Handles POST requests for user registration and order creation.

### `main()`

- Parses command-line arguments.
- Invokes the appropriate command based on the user's input.

## database.py Functions

### `initialize_database()`

- Initializes the SQLite database and creates necessary tables for users, honey types, and orders.
- Inserts sample honey types into the database.

### `create_user(username, email, password)`

- Registers a new user in the database.

### `find_user_by_email(email)`

- Retrieves a user by email from the database.

### `get_all_honey_types()`

- Retrieves all honey types from the database.

### `create_order(user_id, honey_type_id, quantity)`

- Creates a new honey order in the database.

## Contributions

Contributions to this project are welcome. If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---