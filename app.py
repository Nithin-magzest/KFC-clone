from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    db = get_db()
    items = db.execute("SELECT * FROM menu").fetchall()
    return render_template("menu.html", items=items)

@app.route("/order", methods=["POST"])
def order():
    data = request.json
    item = data["item"]

    db = get_db()
    db.execute("INSERT INTO orders(item) VALUES(?)", (item,))
    db.commit()

    return jsonify({"message": "Order placed successfully!"})

if __name__ == "__main__":
    app.run(debug=True)