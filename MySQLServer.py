import mysql.connector
try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      password="yourpassword",
      database="alx_book_store"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    mycursor.execute("USE alx_book_store")
except mysql.connector.Error as err:
    print(f"Error: {err}")    
finally:
    if 'mydb' in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()