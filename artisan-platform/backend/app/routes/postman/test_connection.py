import mysql.connector
from flask import Flask, jsonify

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

if __name__ == '__main__':
    app.run(debug=True)