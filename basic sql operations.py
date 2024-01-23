import sqlite3
import os


def print_all_clients():
    db = sqlite3.connect("dog_walking.db")
    cursor = db.cursor()                            # return file pointer value
    all_content = "SELECT * FROM clients"            # set_up query
    cursor.execute(all_content)
    results = cursor.fetchall()                      # run query
    for client in results:
        print(client)                                # show results of query

    db.close()


def show_dog_gender():
    gender = input("Gender?")
    db = sqlite3.connect("dog_walking.db")
    cursor = db.cursor()
    gender_qry = "SELECT dog_name, dog_gender FROM clients WHERE dog_gender =?;"
    cursor.execute(gender_qry, (gender,))
    results = cursor.fetchall()
    for dog in results:
        print(f"Dog: {dog[0]} Gender: {dog[1]}")

    db.close()


def add_clients():
    db = sqlite3.connect("dog_walking.db")
    cursor = db.cursor()

    f_name = input("First name of new client: ")
    l_name = input("Last name of new client: ")
    p_code = input("Postal code of new client: ")
    d_name = input("Name of dog of new client: ")
    d_gender = input("Gender of dog of new client: ")

    cursor.execute("""INSERT INTO clients(first_name, last_name,
                   post_code, dog_name, dog_gender) VALUES (?,?,?,?,?)""",
                   (f_name, l_name, p_code, d_name, d_gender))

    db.commit()  # add changes to database
    print("Data was added...")
    db.close()


def delete_record():
    db = sqlite3.connect("dog_walking.db")
    cursor = db.cursor()
    remove = input("ID of client to be removed")
    cursor.execute("DELETE FROM clients WHERE client_id == ?", (remove,))
    db.commit()
    db.close()


def edit_field():
    db = sqlite3.connect("dog_walking.db")
    cursor = db.cursor()
    edit_id = input("ID of client whose record you want to edit: ")
    cursor.execute("SELECT * FROM clients WHERE client_id = ?", (id,))
    results = cursor.fetchall()
    os.system('cls')
    print(f"{'1.ID': <3}{'2.FIRST NAME': ^15} {'3.LAST NAME':^15}", end='')
    print(f"{'4.POSTAL CODE': >5} {'5.DOG NAME': >15} {'6.DOG GENDER': <15}")
    for client in results:
        print(f"{client[0]: <8}{client[1]: <15}{client[2]: <15}", end='')
        print(f"{client[3]: <17}{client[4]: <10}{client[5]: <15}")
    field = input("Which field do you want to edit: ")
    new_value = input("Please enter the new value: ")
    if field == "2":
        cursor.execute(
            "UPDATE clients SET first_name = ? WHERE client_id = ?", (new_value, edit_id))
    elif field == "3":
        cursor.execute(
            "UPDATE clients SET last_name = ? WHERE client_id = ?", (new_value, edit_id))
    elif field == "4":
        cursor.execute(
            "UPDATE clients SET post_code = ? WHERE client_id = ?", (new_value, edit_id))
    elif field == "5":
        cursor.execute(
            "UPDATE clients SET dog_name = ? WHERE client_id = ?", (new_value, edit_id))
    elif field == "6":
        cursor.execute(
            "UPDATE clients SET dog_gender = ? WHERE client_id = ?", (new_value, edit_id))
    print("The record was successfully changed...")
    db.commit()
    db.close()


if __name__ == "__main__":
    option = "1"
    while option != "6":
        print("---------MENU----------")
        print("1. Display all clients")
        print("2. Add records")
        print("3. Show dogs according to gender")
        print("4. Remove a record ")
        print("5. Edit a field ")
        print("6. Exit")
        option = input("Choose an option from the menu: ")
        if option == "1":
            print_all_clients()
        elif option == "2":
            add_clients()
        elif option == "3":
            show_dog_gender()
        elif option == "4":
            print_all_clients()
            delete_record()
        elif option == "5":
            print_all_clients()
            edit_field()
