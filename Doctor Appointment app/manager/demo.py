import mysql.connector

# Connect to the MySQL database
def connect_to_database():
    try:
        conn=mysql.connector.connect(host='localhost',username='root',password='Admin@123',database='mydata')

        
        print("Connected to the database.")
        return conn
    except mysql.connector.Error as error:
        print("Error while connecting to the database: ", error)
        return None

# Fetch data from the database
def fetch_data(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM doctor")
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except mysql.connector.Error as error:
        print("Error while fetching data from the database: ", error)
        return []

# Write data to a file
def write_to_file(data):
    try:
        with open("output.txt", "w") as file:
            for row in data:
                file.write(str(row) + "\n")
        print("Data written to the file: output.txt")
    except IOError as error:
        print("Error while writing to the file: ", error)

# Click event handler for fetching and writing data
def button_click():
    conn = connect_to_database()
    if conn:
        data = fetch_data(conn)
        write_to_file(data)
        conn.close()

# Button click simulation
button_click()
