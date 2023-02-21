import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="bacchus_user",
    passwd="abc123",
    database="bacchus_winery"  #any info will go into this database
)

mycursor = mydb.cursor()


#display customers
query = "SELECT * from customer"
mycursor.execute(query)
result = mycursor.fetchall()
print("--DISPLAYING CUSTOMERS--")
for row in result:
    print("Customer ID:", row[0])
    print("First Name:", row[1])
    print("Last Name:", row[2])
    print("Email:", row[3])
    print("Address:", row[4])
    print("City:", row[5])
    print("State:", row[6])
    print("Zipcode:", row[7])
    print(" ")


#display customer orders
query = "SELECT * from customerorder"
mycursor.execute(query)
result = mycursor.fetchall()
print("--DISPLAYING EMPLOYEE RECORDS--")
for row in result:
    print("Customer Order ID:", row[0])
    print("Customer ID:", row[1])
    print("Product ID:", row[2])
    print("QTY:", row[3])
    print(" ")


#display employee records
query = "SELECT * from employee"
mycursor.execute(query)
result = mycursor.fetchall()
print("--DISPLAYING EMPLOYEE RECORDS--")
for row in result:
    print("Employee ID:", row[0])
    print("Role ID:", row[1])
    print("First Name:", row[2])
    print("Last Name:", row[3])
    print(" ")

#display Paycheck
query = "SELECT * from paycheck"
mycursor.execute(query)
result = mycursor.fetchall()
print("--DISPLAYING PAYCHECK RECORDS--")
for row in result:
    print("Paycheck ID:", row[0])
    print("Hours:", row[1])
    print("Rate:", row[2])
    print("Start Date:", row[3])
    print("End Date:", row[4])
    print("Employee ID:", row[5])
    print(" ")

#display roles
query = "SELECT * from role"
mycursor.execute(query)
result = mycursor.fetchall()
print("--DISPLAYING ROLES--")
for row in result:
    print("Role ID:", row[0])
    print("Comments:", row[1])
    print(" ")

#display products
query = "SELECT * from product"
mycursor.execute(query)
result = mycursor.fetchall()
print("--DISPLAYING PRODUCTS--")
for row in result:
    print("Product ID:", row[0])
    print("Product Name:", row[1])
    print("Price:", row[3])
    print("Quantity on hand:", row[4])
    print(" ")


# close the cursor
mycursor.close()
# close the connection
mydb.close()
