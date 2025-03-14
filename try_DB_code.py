import mysql.connector

def store_user_data(username, email, password):
    """Connects to a MySQL database and stores user data.

    Args:
        username (str): The user's username.
        email (str): The user's email address.
        password (str): The user's password.
    """

    try:
        # 1. Database Connection (Replace with your XAMPP MySQL credentials)
        mydb = mysql.connector.connect(
            host="localhost",  # Usually "localhost" for XAMPP
            user="root",      # Default XAMPP MySQL user
            password="",      # Default XAMPP MySQL password (often blank)
            database="python" # Replace with your database name
        )

        mycursor = mydb.cursor()

        # 2. SQL Query (Insert data)
        sql = "INSERT INTO py_table (username, email, password) VALUES (%s, %s, %s)"
        val = (username, email, password)

        # 3. Execute Query
        mycursor.execute(sql, val)
        mydb.commit()  # Commit the changes

        print(mycursor.rowcount, "record inserted.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Ensure the connection is closed
        if 'mydb' in locals() and mydb.is_connected(): # Check if mydb exists and is connected.
           mycursor.close()
           mydb.close()
           print("MySQL connection closed.")

# Example Usage (Get user input)
if __name__ == "__main__":
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")  # In a real app, hash the password!

    store_user_data(username, email, password)