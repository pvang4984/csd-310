import mysql.connector

#user validation
connection = mysql.connector.connect(  #saves the connection in 'connection' variable
    user='movies_user', password='popcorn',  #verifys credentials and links to movies database
    host='localhost',
    database='Movies')

cursor = connection.cursor()


def show_films(cursor, title):
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name', from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    films = cursor.fetchall()
    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[3]))

# close the cursor
cursor.close()
# close the connection
connection.close()
