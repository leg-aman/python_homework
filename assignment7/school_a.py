import sqlite3

# connect to a new SQLite database
with sqlite3.connect("../db/school.db") as conn:
    # create the file here, so that it is not pushed to GitHub!
    print("Database created and connected successfully!")

# The "with" statement closes the connection at the end of that block. You could close it explicitly with conn.close(),
# but it this case the "with" statement takes care of that.