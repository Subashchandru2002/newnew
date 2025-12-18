import sqlite3

def get_user_data(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # VULNERABILITY: SQL Injection (string formatting instead of parameterized query)
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    
    cursor.execute(query)
    return cursor.fetchone()
