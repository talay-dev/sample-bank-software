import sqlite3

def open_database():
    return sqlite3.connect('database.db')

#create a table in the database with name, surname, age, client number and password if it exists already, return an error message
def create_table():
    conn = open_database()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clients (name text, surname text, age integer, client_number integer, password text, balance real)''')
    conn.commit()
    conn.close()

#add a new client to the database
def add_client(name, surname, age, client_number, password, balance=0):
    conn = open_database()
    c = conn.cursor()
    c.execute("INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?)", (name, surname, age, client_number, password, balance))
    conn.commit()
    conn.close()

#delete a client from the database using the client number
def delete_client(client_number):
    conn = open_database()
    c = conn.cursor()
    c.execute("DELETE FROM clients WHERE client_number = ?", (client_number,))
    conn.commit()
    conn.close()

#update a client's details in the database using the client number
def update_client(name, surname, age, client_number, password, balance):
    conn = open_database()
    c = conn.cursor()
    c.execute("UPDATE clients SET name = ?, surname = ?, age = ?, password = ?, balance = ? WHERE client_number = ?", (name, surname, age, password, client_number, balance))
    conn.commit()
    conn.close()

#search for a client in the database using the client number
def search_client(client_number):
    conn = open_database()
    c = conn.cursor()
    c.execute("SELECT * FROM clients WHERE client_number = ?", (client_number,))
    client = c.fetchone()
    conn.close()
    return client


# a function that change only the balance of a client in the database
def update_balance(client_number, balance):
    conn = open_database()
    c = conn.cursor()
    c.execute("UPDATE clients SET balance = ? WHERE client_number = ?", (balance, client_number))
    conn.commit()
    conn.close()

def get_all_clients():
    conn = open_database()
    c = conn.cursor()
    c.execute("SELECT * FROM clients")
    clients = c.fetchall()
    conn.close()
    return clients
    


#return all clients in the database with a specific name

