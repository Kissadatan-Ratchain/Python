import sqlite3
import database

CREATE_USERS_TABLE = "CREATE TABLE IF NOT EXISTS users(id INTGER PRIMARY KEY, name TEXT, product TEXT, price INTEGER);"

INSERT_USERS = "INSERT INTO users (name, product, price) VALUES (?, ?, ?);"

GET_ALL_USERS = "SELECT * FROM users;"

USERS_BY_NAME = "SELECT * FROM users WHERE name = ?;"

BEST_FOR_USERS = """
SELECT * FROM users
WHERE name = ?
ODER BY price DESC
LIMIT 1;"""

def connect():
    return sqlite3.connect(r"C:\Users\Lenovo\Desktop\py\projectsql.db")

def create_table(connection):
    with connection:
        connection.execute(CREATE_USERS_TABLE)

def add_users(connection, name, product, price):
    with connection:
        connection.execute(INSERT_USERS, (name, product, price))

def get_all_users(connection):
    with connection:
       return connection.execute(GET_ALL_USERS).fetchall()

def users_by_name(connection, name):
    with connection:
       return connection.execute(USERS_BY_NAME, (name,)).fetchall()

def best_for_users(connection, name):
    with connection:
        return connection.execute(BEST_FOR_USERS,(name,)).fetchone()

def menu():

    print("---coffee shop---")
    print("-----------------------")
    print("Please select option")
    print("1.Add a new oder.")
    print("2.See all oder.")
    print("3.Find user by name.")
    print("4.See which best product for user.")
    print("5.Edit data")
    print("6.Exit")
    print("-----------------------")

def add_users():    

    name = input("Enter user name: ")
    product = input("What do you need: ")
    price = int(input("Enter your price: "))

    database.add_users(connection,name, product, price)

def see_all():
    conn = sqlite3.connect(r"C:\Users\Lenovo\Desktop\py\projectsql.db")
    c = conn.cursor()

    c.execute('''SELECT * FROM users''')

    result = c.fetchall()
    for x in result:
        print(x)

def find_user():

    name = input("Enter user name to find: ")
    conn = sqlite3.connect(r"C:\Users\Lenovo\Desktop\py\projectsql.db")
    c = conn.cursor()

    c.execute('''SELECT * FROM users WHERE name = ?''',(name,))
    result = c.fetchone()
            
    print(result)

def product_user():
    name = input("Enter user name to find: ")
    name = [name,]
    conn = sqlite3.connect(r"C:\Users\Lenovo\Desktop\py\projectsql.db")
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name = ?',name)
    result = c.fetchone()
    print("Your name in put is",result[1])
    print("Product is",result[2])

def edit_data():
    print("----edit data----")
    num = input("input number to edit")
    name = input("input name to edit:")
    product = input("input product to edit:")
    price = input("input price to edit:")
    data = (name,product,price,'{}'.format(num))
    conn = sqlite3.connect(r"C:\Users\Lenovo\Desktop\py\projectsql.db")
    c = conn.cursor()
    c.execute('''UPDATE users SET name = ?,product = ?, price = ? WHERE id = ?''',data)
    conn.commit()
    print("edit done!")

while True:
    menu()

    user_input = input("Please select number:")
    if user_input == '1':
        add_users()
        
    elif user_input == '2':
        see_all()

    elif user_input == '3':
        find_user()
            
    elif user_input == '4':
        product_user()
        
    elif user_input == '5':
        edit_data()

    elif user_input == '6':
        break

    else:
        print("Please try again!")


menu()
