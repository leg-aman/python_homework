# Task: Create a New SQLite Database
import sqlite3
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        print("Database created and connected successfully!")

# Task: Define Database Structure
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS publishers (
                   publisher_id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL UNIQUE
                   )
                   """)
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS magazines (
                   magazine_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE,
                    publisher_id INTEGER NOT NULL,
                    FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
                   )
                   """)
    cursor.execute("""
                     CREATE TABLE IF NOT EXISTS subscribers (
                    subscriber_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        address TEXT NOT NULL
                   )
                   """)
    cursor.execute("""
                     CREATE TABLE IF NOT EXISTS subscriptions (
                        subscription_id INTEGER PRIMARY KEY,
                        subscriber_id INTEGER NOT NULL,
                        magazine_id INTEGER NOT NULL,
                        expiration_date TEXT NOT NULL,
                        FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
                        FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
                   )
                   """)
    print("Tables created successfully!")

# Task 3: Populate Tables with Data
    conn.execute("PRAGMA foreign_keys = 1")
    def add_publisher(cursor, name):
        try:
            cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        except sqlite3.IntegrityError:
            print(f"Publisher '{name}' already exists.")
    def add_magazine(cursor, name, publisher_id):
        try:
            cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        except sqlite3.IntegrityError:
            print(f"Magazine '{name}' already exists.")
    def add_subscriber(cursor, name, address):
        try:
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        except sqlite3.IntegrityError:
            print(f"Subscriber '{name}' already exists.")
    def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
        try:
            cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                           (subscriber_id, magazine_id, expiration_date))
        except sqlite3.IntegrityError:
            print(f"Subscription for subscriber ID {subscriber_id} and magazine ID {magazine_id} already exists.")

# Insert sample data into the tables
    cursor = conn.cursor()

# Publishers
    add_publisher(cursor,"Tech Publishing")
    add_publisher(cursor,"Health & Wellness Publishing")
    add_publisher(cursor,"Travel & Leisure Publishing")

# Magazines
    add_magazine(cursor,"Tech Today", 1)
    add_magazine(cursor,"Health Monthly", 2)
    add_magazine(cursor,"Travel Explorer", 3)

# Subscribers
    add_subscriber(cursor,"Alice Smith", "123 Elm St, Springfield")
    add_subscriber(cursor,"Bob Johnson", "456 Oak St, Springfield")
    add_subscriber(cursor,"Charlie Brown", "789 Pine St, Springfield")

# Subscriptions
    add_subscription(cursor,1, 1, "2024-12-31")
    add_subscription(cursor,2, 2, "2024-11-30")    
    add_subscription(cursor,3, 3, "2024-10-31")

    conn.commit()
    print("Sample data inserted successfully!")

# Task 4: Write SQL Queries
    cursor.execute("select * from subscribers")
    rows = cursor.fetchall()
    print("Subscribers:")
    for row in rows:
        print(row)
    
    cursor.execute("select * from magazines order by name")
    rows = cursor.fetchall()
    print("Magazines:")
    for row in rows:
        print(row)

    cursor.execute("select magazines.name, publishers.name from magazines join publishers on magazines.publisher_id = publishers.publisher_id")
    rows = cursor.fetchall()
    print("Magazines and their publishers:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

