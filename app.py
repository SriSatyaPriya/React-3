import psycopg2
from flask import Flask, request

app = Flask(_name_)

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="your_db_name",
    user="your_db_user",
    password="your_db_password"
)

@app.post("/login")
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    cur = conn.cursor()
    cur.execute("SELECT Password FROM User WHERE User=%s", (username,))
    result = cur.fetchone()

    if not result:
        return "User not found"

    db_password = result[0]
    if db_password == password:
        return "Login Successful!"
    else:
        return "Incorrect Password"

if _name_ == "_main_":
    app.run(debug=True)