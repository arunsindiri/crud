import sqlite3

def get_connection():
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            age INTEGER NOT NULL, 
            course TEXT NOT NULL)
    """)

    connection.commit()
    connection.close()

def adding_student(name, age, course):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students(name, age, course)
        VALUES (?, ?, ?)""", (name, age, course))

    connection.commit()
    connection.close()

def student_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM students WHERE id = ?""", (id,))

    student = cursor.fetchone()
    connection.close()

    if student:
        return dict(student)
    return None
    
def get_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM students""")
    students = cursor.fetchall()
    connection.close()

    student_list = []
    for student in students:
        student_dict = dict(student)
        student_list.append(student_dict)
    return student_list
    
