# **Inventory Management System (IMS)**

## **📌 Overview**
The **Inventory Management System (IMS)** is a **console-based application** built using **Python, MySQL, and MVC architecture**.  
It allows multiple admins to **register, log in, and manage their own inventory of products**.  
Each admin can **add, update, view, and delete their own products**, and products of other admins remain hidden.

---

## **✨ Features**
✔ **User Authentication** (Register & Login with `bcrypt` password hashing)  
✔ **Admin-specific Product Management**  
✔ **Add, Update, and Remove Products**  
✔ **View Only Your Products**  
✔ **Low Stock Alert** (quantity < 5)  
✔ **Foreign Key Relationship between Users and Products**  
✔ **Secure Authentication & SQL Injection Prevention**  

---

## **🛠 Tech Stack**
- **Language:** Python  
- **Database:** MySQL  
- **Architecture:** MVC (Model-View-Controller)  
- **Libraries:**  
  - `mysql-connector-python` → Database connectivity  
  - `bcrypt` → Password hashing  

---

## **📂 Project Structure**
IMS/
│
├── connect_db.py # Handles DB connection
├── model.py # Model layer (Database operations)
├── view.py # View layer (Menus & user input)
├── controller.py # Controller layer (Business logic)
└── README.md # Project documentation

pgsql
Copy
Edit

---

## **⚙️ Database Schema**
### **users table**
| Column    | Type          | Constraint                |
|-----------|---------------|---------------------------|
| id        | INT           | PRIMARY KEY, AUTO_INCREMENT |
| username  | VARCHAR(50)   | UNIQUE, NOT NULL         |
| email     | VARCHAR(100)  | UNIQUE, NOT NULL         |
| password  | VARCHAR(255)  | NOT NULL                |

### **products table**
| Column    | Type           | Constraint                            |
|-----------|---------------|--------------------------------------|
| id        | INT           | PRIMARY KEY, AUTO_INCREMENT         |
| name      | VARCHAR(50)   | NOT NULL                            |
| price     | DECIMAL(10,2) | NOT NULL                            |
| quantity  | INT           | NOT NULL                            |
| user_id   | INT           | FOREIGN KEY REFERENCES users(id) ON DELETE CASCADE |

---

## **🔗 Relationships**
- One **user** can have multiple **products**.
- Products are linked to users using `user_id` as a foreign key.

---

## **🚀 How to Run**
### **1. Clone the repository**
```bash
git clone https://github.com/your-username/ims-project.git
cd ims-project
2. Install dependencies
bash
Copy
Edit
pip install mysql-connector-python bcrypt
3. Configure Database
Create a database in MySQL:

sql
Copy
Edit
CREATE DATABASE ims_db;
Update your connect_db.py with your MySQL credentials:

python
Copy
Edit
import mysql.connector

def sql_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",
        password="your_mysql_password",
        database="ims_db"
    )
4. Run the application
bash
Copy
Edit
python controller.py
📜 Menu Flow
Authentication Menu

markdown
Copy
Edit
1. Register
2. Login
3. Exit
Inventory Menu (After Login)

mathematica
Copy
Edit
1. Add Product
2. Remove Product
3. Update Product Quantity
4. View Products
5. Check Low Stock
6. Logout
