import mysql.connector

#Establish a connection to the MySQL database
conn = mysql.connector.connnect(host="localhost",
    user="root",
    password= "68078183",
    database="prison_management")

#Create a cursor object to interact with the database
cursor = conn.cursor()

#Create a table for prisoners
cursor.execute("""
    CREATE TABLE ID NOT EXISTS prisoners (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        crime VARCHAR(255),
        address VARCHAR(255),
        cell_number INT,
        article VARCHAR(255),
        marital_status VARCHAR(255),
        release_date DATE)""")

#Insert a prisoner's information into the database
def add_prisoner(firstt_name, last_name, age, crime, address, cell_number, article, marital_status, release_date):
    sql = "INSERT INTO prisoners (first_name, last_name, age, crime, address, cell_number, article, marital_status, release_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (first_name, last_name, age, crime, address, cell_number, article, marital_status, release_date)
    cursor.execute(sql, val)
    conn.commit()
    print("Prisoner added successfully")

#Inserting data of prisoners
n = "Yes"
while n!="No":
    first_name=input("Enter first name of prisoner: ")
    last_name=input("Enter last name of prisoner: ")
    for i in range(0, 80):
        print("=", end="")
    print()
    age=int(input("Enter age of prisoner: "))
    for i in range(0, 80):
        print("=", end="")
    print()
    crime=input("Enter crime of prisoner: ")
    for i in range(0, 80):
        print("=", end="")
    print()
    address=input("Enter address of prisoner: ")
    for i in range(0, 80):
        print("=", end="")
    print()
    cell_number=int(input("Enter cell number of prisoner: "))
    for i in range(0, 80):
        print("=", end="")
    print()
    article=input("Enter article under which prisoner is arrested: ")
    for i in range(0, 80):
        print("=", end="")
    print()
    marital_status=input("Enter marital status of prisoner: ")
    for i in range(0, 80):
        print("=", end="")
    print()
    release_date=input("Enter release of prisoner (YYYY-MM-DD): ")
    for i in range(0, 80):
        print("=", end="")
    print()
    add_prisoner(first_name, last_name, age, crime, address, cell_number, article, marital_status, release_date)
    print()
    n=input("Do you want to add more prisoners (Yes/No): ")
    print()
print("All prisoners added successfully!!")

#Close the cursor and the database connection
cursor.close()
conn.close()
