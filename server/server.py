from flask import Flask, request, jsonify, session
from flask_mysqldb import MySQL
from flask_cors import CORS 
from werkzeug.security import generate_password_hash, check_password_hash
import MySQLdb.cursors
import cred #credential file DO NOT push

#app instance
app = Flask(__name__)
app.secret_key = 'superrsecret keyyyyy'
CORS(app) #Cors policy so FE can fetch API 

#DB connector
app.config['MYSQL_HOST'] = cred.host
app.config['MYSQL_PORT'] = cred.port
app.config['MYSQL_USER'] = cred.user
app.config['MYSQL_PASSWORD'] = cred.password
app.config['MYSQL_DB'] = cred.db
mysql = MySQL(app)

#Route
@app.route("/hello", methods=['GET'])
def home():
    return jsonify([{
        'name':"Kaisa",
        'age' :"20"
    },
    {
        'name':"Danh",
        'age' :"25"
    }])
       
@app.route("/test", methods=['GET'])
def testSQL():
    #Creating a connection cursor
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    #Executing SQL Statements
    cursor.execute("SELECT * FROM users")
    column_names=[x[0] for x in cursor.description] # Get columns name
    data = cursor.fetchall()
    cursor.close()
    
    json_data = []
    for result in data:
        json_data.append(dict(zip(column_names,result)))
    return jsonify(json_data)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    account = cursor.fetchone()
    if account:
        cursor.close()
        return jsonify({'status': 'fail', 'message': 'Account already exists!'}), 200
    else:
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'status': 'success', 'message': 'You have successfully registered!'}), 200


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
    account = cursor.fetchone()
    cursor.close()
    
    if account:
        session['username'] = account['username']
        message = f"hello {session['username']}"
        return jsonify({'status': 'success', 'message': message}), 200
    else:
        cursor.close()
        return jsonify({'status': 'fail', 'message': 'Incorrect username/password!'}), 401
    
@app.route("/check", methods=['GET'])
def checksession():
    username = session.get('username')
    if username:
        message = f"Hello, {username}"
    else:
        message = "No active session"
    return jsonify({'status': 'success', 'message': message}), 200
            
if __name__ == "__main__":
    app.run(host="localhost", port=8001, debug=True)
    
    
    