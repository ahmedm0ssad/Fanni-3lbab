import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Update with your MySQL database configuration
db_config = {
    'user': 'Rana',
    'password': 'Rana-555',
    'host': 'localhost',
    'database': 'Fanni_3lbab'
}

@app.route('/test_db_connection', methods=['GET'])
def test_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        cursor.close()
        connection.close()
        return jsonify({"detail": f"Connected to database: {db_name[0]}"}), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@app.route('/users', methods=['GET'])
def read_users():
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users LIMIT %s OFFSET %s", (limit, skip))
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(users), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO users (address, created_at, email, name, password_hash, phone, updated_at, user_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                user_data['address'],
                user_data['created_at'],
                user_data['email'],
                user_data['name'],
                user_data['password_hash'],
                user_data['phone'],
                user_data['updated_at'],
                user_data['user_type']
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"detail": "User created successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        if user is None:
            return jsonify({"detail": "User not found"}), 404
        return jsonify(user), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

if __name__ == '__main__':
    app.run(debug=True)