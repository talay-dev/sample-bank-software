import db 
import random

open_database = db.open_database

#a function that generates a random client number for a new client and checks if it already exists in the database 
def generate_client_number():
    import random
    client_number = random.randint(1000, 9999)
    conn = open_database()
    c = conn.cursor()
    c.execute("SELECT * FROM clients WHERE client_number = ?", (client_number,))
    client = c.fetchone()
    conn.close()
    if client is None:
        return client_number
    else:
        generate_client_number()

#generate a random password for a new client
def generate_password():
    import random
    password = random.randint(1000, 9999)
    return password

#add a new client to the database
def add_client(name, surname, age , balance=0):
    client_number = generate_client_number()
    password = generate_password()
    db.add_client(name, surname, age, client_number, password , balance)
    print("Client added successfully!")
    print("Client number: ", client_number)
    print("Password: ", password)

#delete a client from the database using the client number
def delete_client(client_number):
    db.delete_client(client_number)
    print("Client deleted successfully!")

#update a client's details in the database using the client number
def update_client(name, surname, age, client_number, password, balance):
    db.update_client(name, surname, age, client_number, password, balance)
    print("Client updated successfully!")

#search for a client in the database using the client number
def search_client(client_number):
    client = db.search_client(client_number)
    if client is not None:
        print("Client found!")
        print("Name: ", client[0])
        print("Surname: ", client[1])
        print("Age: ", client[2])
        print("Client number: ", client[3])
        print("Password: ", client[4])
        print("Balance: ", client[5])
    else:
        print("Client not found!")



