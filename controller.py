from model import Model
from view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.current_user_id = None

    def run(self):
        while True:
            choice = self.view.show_auth_menu()

            if choice == "1":
                username, email, password = self.view.show_registration_menu()
                if self.model.register_user(username, email, password):
                    self.view.display_message("✅ Registration successful! You can now log in.")
                else:
                    self.view.display_message("❌ Registration failed! Username or email may already exist.")
            elif choice == "2":
                username, password = self.view.show_login_menu()
                user_id = self.model.authenticate_user(username, password)
                if user_id:
                    self.current_user_id = user_id
                    self.view.display_message("✅ Login successful!")
                    self.view.display_message(f"Welcome, {username}")
                    self.show_inventory_menu()
                else:
                    self.view.display_message("❌ Invalid credentials! Please try again.")
            elif choice == "3":
                self.view.display_message("👋 Exiting system...")
                break
            else:
                self.view.display_message("❌ Invalid choice! Please select a valid option.")

    def show_inventory_menu(self):
        while True:
            choice = self.view.show_main_menu()

            if choice == "1":
                name, price, quantity = self.view.get_product_details()
                try:
                    self.model.add_product(self.current_user_id, name, float(price), int(quantity))
                    self.view.display_message("✅ Product added successfully!")
                except ValueError:
                    self.view.display_message("❌ Invalid price or quantity! Please enter numeric values.")
            elif choice == "2":
                product_id = self.view.get_product_id()
                if self.model.remove_product(self.current_user_id, product_id):
                    self.view.display_message("✅ Product removed successfully!")
                else:
                    self.view.display_message("❌ Product not found or unauthorized access!")
            elif choice == "3":
                product_id = self.view.get_product_id()
                new_quantity = self.view.get_new_quantity()
                if self.model.update_product_quantity(self.current_user_id, product_id, new_quantity):
                    self.view.display_message("✅ Product quantity updated successfully!")
                else:
                    self.view.display_message("❌ Product not found or unauthorized access!")
            elif choice == "4":
                products = self.model.get_products(self.current_user_id)
                self.view.display_products(products)
            elif choice == "5":
                low_stock = self.model.check_stock(self.current_user_id)
                for product in low_stock:
                    self.view.show_stock_alert(product[1], product[3])
            elif choice == "6":
                self.view.display_message("🔒 Logging out...")
                self.current_user_id = None
                break
            else:
                self.view.display_message("❌ Invalid choice! Please select a valid option.")
