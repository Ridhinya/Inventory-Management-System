import getpass
class View:
    def show_auth_menu(self):
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        return input("Choose an option: ")

    def show_registration_menu(self):
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = getpass.getpass("Enter password: ")
        return username, email, password

    def show_login_menu(self):
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        return username, password

    def show_main_menu(self):
        print("\n1. Add Product")
        print("2. Remove Product")
        print("3. Update Product Quantity")
        print("4. Display Products")
        print("5. Check Low Stock Alerts")
        print("6. Logout")
        return input("Choose an option: ")

    def get_product_details(self):
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        quantity = input("Enter product quantity: ")
        return name, price, quantity

    def get_product_id(self):
        return input("Enter product ID: ")

    def get_new_quantity(self):
        return input("Enter new quantity: ")

    def display_products(self, products):
        print("\nInventory Products:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}")
        if not products:
            print("No products found.")

    def show_stock_alert(self, product_name, quantity):
        print(f"⚠️ ALERT: Product '{product_name}' has low stock ({quantity} left)!")

    def display_message(self, message):
        print("\n" + message)
