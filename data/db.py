import sqlite3 

def create_table():
    try:
        sql_con = sqlite3.connect("pizzas.db")
        cursor = sql_con.cursor()

        with open("create.db.sql") as file:
            query = file.read()

        cursor.execute(query)
        sql_con.commit()
        cursor.close()
        print("Дані успішно записані")

    except sqlite3.Error as error:
        print(f"{error = }")

    finally:
        if sql_con:
            sql_con.close()
            print("Робота з базою даних успішно завершена")


def insert_data(
    name: str,
    price: int,
    ingredients: str|None = None
    ) -> None:

    try:
        sql_con = sqlite3.connect("pizzas.db")
        cursor = sql_con.cursor()

        query = "INSERT INTO Pizzas (name, price, ingredients) VALUES (?, ?, ?)"
        data = (name, price, ingredients)

        cursor.execute(query, data)
        sql_con.commit()
        cursor.close()
        print("Дані успішно записані")

    except sqlite3.Error as error:
        print(f"{error = }")

    finally:
        if sql_con:
            sql_con.close()
            print("Робота з базою даних успішно завершена")
            
def get_pizzas():

    try:
        sql_con = sqlite3.connect("pizzas.db")
        cursor = sql_con.cursor()

        query = "SELECT * FROM Pizzas"

        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        print("Дані успішно записані")

    except sqlite3.Error as error:
        print(f"{error = }")

    finally:
        if sql_con:
            sql_con.close()
            print("Робота з базою даних успішно завершена")
    
    return data