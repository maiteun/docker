from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='database',         # Docker Compose에서 설정한 MySQL 서비스 이름
        user='exampleuser',      # Docker Compose에서 설정한 사용자 이름
        password='examplepassword',  # Docker Compose에서 설정한 비밀번호
        database='exampledb'     # Docker Compose에서 설정한 데이터베이스 이름
    )
    return connection

@app.route('/students', methods=['GET'])
def get_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
