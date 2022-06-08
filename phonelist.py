#import sqlite3
#conn = sqlite3.connect("phone.db")


import psycopg2
conn = psycopg2.connect(
host="localhost",
database="phone",
user="phone",
password="abc123"
)

def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}', '{address}');")
    cur.close()
def delete_phone(C, name, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}' AND ID = '{ID}';")
    cur.close()
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
        print("Phonelist saved!")
    except:
        print("No changes!")
    cur.close()
print("Hello and welcome to the phone list, available commands: \n add - add a phone number \n delete - delete a contact \n list - list all phone numbers \n quit - quit the program \n save - save the program \n help - commandslist")
while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").upper()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        address = input(" Address: ")
        add_phone(conn, name, phone)
    elif cmd == "DELETE":
        name = input("  Name: ")
        id = input(" ID: ")
        delete_phone(conn, name, 'ID')
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
    elif cmd == "SAVE":
        save_phonelist(conn)
    elif cmd == "HELP":
        print("Available commands: \n add - add a phone number \n delete - delete a contact \n list - list all phone numbers \n quit - quit the program \n save - save the program \n help - commandslist")      
    else:
        print(f"Unknown command: '{cmd}'")
