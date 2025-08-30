from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "flaskdb"),
        user=os.environ.get("DB_USER", "flaskuser"),
        password=os.environ.get("DB_PASSWORD", "flaskpass"),
        port=os.environ.get("DB_PORT", "5432")
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM items;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    items_list = []
    for row in rows:
        items_list.append({'id': row[0], 'name': row[1]})
    return jsonify(items_list)

@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    name = data.get('name')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name) VALUES (%s) RETURNING id;", (name,))
    item_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": item_id, "name": name}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)