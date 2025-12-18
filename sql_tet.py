import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/user')
def get_user():
    # SOURCE: User input from a URL parameter
    user_id = request.args.get('id')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # SINK: Input is used directly in a string-formatted query
    # This should trigger: "Query built from user-controlled sources"
    query = "SELECT * FROM profiles WHERE id = '%s'" % user_id
    cursor.execute(query)
    
    return str(cursor.fetchone())
