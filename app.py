import os
import time
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL config
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'mysql')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'admin')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'admin')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'tws_db')

mysql = MySQL(app)

# ✅ Retry logic for DB
def init_db():
    retries = 10

    while retries > 0:
        try:
            print("⏳ Trying to connect to MySQL...")

            with app.app_context():   # ✅ REQUIRED FIX
                cur = mysql.connection.cursor()
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS messages (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        message TEXT
                    );
                ''')
                mysql.connection.commit()
                cur.close()

            print("✅ Database initialized")
            return

        except Exception as e:
            print(f"❌ DB not ready: {e}")
            retries -= 1
            time.sleep(5)

    print("❌ Could not connect to DB. Exiting...")
    exit(1)


@app.route('/')
def hello():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT message FROM messages')
        messages = cur.fetchall()
        cur.close()
        return render_template('index.html', messages=messages)
    except Exception as e:
        return f"Database Error: {e}"


@app.route('/submit', methods=['POST'])
def submit():
    try:
        new_message = request.form.get('new_message')
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO messages (message) VALUES (%s)', [new_message])
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': new_message})
    except Exception as e:
        return f"Insert Error: {e}"


if __name__ == '__main__':
    init_db()
    print("🚀 Starting Flask app...")
    app.run(host='0.0.0.0', port=5000, debug=False)
