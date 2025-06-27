#!/usr/bin/env python3
import mysql.connector

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password'  # Replace with your MySQL root password
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        # Create the database if it doesn't exist (no SELECT or SHOW)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close cursor if it was created
    if 'cursor' in locals():
        cursor.close()
    # Close connection if it was established
    if 'connection' in locals() and connection.is_connected():
        connection.close()
