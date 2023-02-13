import mysql.connector

#user validation
connection = mysql.connector.connect( #saves the connection in 'connection' variable
    user='movies_user', password='popcorn', #verifys credentials and links to movies database
    host='localhost',
    database='Movies')

cursor = connection.cursor()

query = "SELECT * from studio" #retrieves data from studio table

# execute the operation stored in the query variable and fetches all rows from the last executed statement
cursor.execute(query)
result=cursor.fetchall()

#display studio records
print("--DISPLAYING Studio RECORDS--")
for row in result:
    print("Studio ID:",row[0])
    print("Studio Name:",row[1])
    print(" ")


#display genre records
query = "SELECT * from genre"
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Genre RECORDS--")
for row in result:
    print("Genre ID:",row[0])
    print("Genre Name:",row[1])
    print(" ")


#display  films whose runtime is less than 2 hours(120 minutes)
query = "SELECT film_name,film_runtime from film where film_runtime<120 "
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Short Film RECORDS--")
for row in result:
    print("Film Name:",row[0])
    print("Runtime:",row[1])
    print(" ")


#display directors info in the order of their name
query = "SELECT film_name,film_director from film order by film_director "
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Director RECORDS in Order--")
for row in result:
    print("Film Name:",row[0])
    print("Director:",row[1])
    print(" ")


# close the cursor
cursor.close()
# close the connection
connection.close()


