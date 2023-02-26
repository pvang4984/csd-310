import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="bacchus_user",
    passwd="abc123",
    database="bacchus_winery"  #any info will go into this database
)

mycursor = mydb.cursor()

#display hours from last 4 quarters
query = "SELECT * from hoursYTD WHERE year > 2021"
mycursor.execute(query)
result = mycursor.fetchall()
print("--DISPLAYING HOURS WORKED LAST 4 QUARTERS RECORDS--")
for row in result:
    print("Year:", row[0])
    print("Employee ID:", row[1])
    print("January Hours:", row[2])
    print("February Hours:", row[3])
    print("March Hours:", row[4])
    print("April Hours:", row[5])
    print("May Hours:", row[6])
    print("June Hours:", row[7])
    print("July Hours:", row[8])
    print("August Hours:", row[9])
    print("September Hours:", row[10])
    print("October Hours:", row[11])
    print("November Hours:", row[12])
    print("December Hours:", row[13])
    totalhours = row[2]+row[3]+row[4]+row[5]+row[6]+row[7]+row[8]+row[9]+row[10]+row[11]+row[12]+row[13]
    print("Total Hours:")
    print(totalhours)
    print("")



# display customer orders
query = "SELECT customerorder.productid, customerorder.quantity, product.productname from customerorder INNER JOIN product ON customerorder.productID = product.productID  WHERE customerorder.productid = 1 "
mycursor.execute(query)
result = mycursor.fetchall()
print("--DISPLAYING Merlot order quantities INFO--")
for row in result:
    print("Product Name:", row[2])
    print("QTY:", row[1])

print(" ")

query = "SELECT customerorder.productid, customerorder.quantity, product.productname from customerorder INNER JOIN product ON customerorder.productID = product.productID  WHERE customerorder.productid = 2 "
mycursor.execute(query)
result = mycursor.fetchall()
print("--DISPLAYING Cabernet order quantities INFO--")
for row in result:
    print("Product Name:", row[2])
    print("QTY:", row[1])

print(" ")

query = "SELECT customerorder.productid, customerorder.quantity, product.productname from customerorder INNER JOIN product ON customerorder.productID = product.productID  WHERE customerorder.productid = 3 "
mycursor.execute(query)
result = mycursor.fetchall()
print("--DISPLAYING Chablis order quantities INFO--")
for row in result:
    print("Product Name:", row[2])
    print("QTY:", row[1])

print(" ")

query = "SELECT customerorder.productid, customerorder.quantity, product.productname from customerorder INNER JOIN product ON customerorder.productID = product.productID  WHERE customerorder.productid = 4 "
mycursor.execute(query)
result = mycursor.fetchall()
print("--DISPLAYING Chardonnay order quantities INFO--")
if row in result:
    print("Product Name:", row[2])
    print("QTY:", row[1])



#display supply order
query = "SELECT supplyorder.supplyorderid, supplyorder.dateplaced, supplyshipment.supplyorderid, supplyshipment.dateshipped from supplyorder INNER JOIN supplyshipment ON supplyorder.supplyorderid = supplyshipment.supplyorderid"
mycursor.execute(query)
result = mycursor.fetchall()
print("--DISPLAYING Supply order placement and Supply order shipment INFO--")
for row in result:
    print(f"Supply order ID {row[0]} placed on {row[1]} was shipped on {row[3]}")





# close the cursor
mycursor.close()
# close the connection
mydb.close()
