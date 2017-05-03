#Sqlite3 DB for Capstone Team6
import sqlite3
from datetime import date, datetime

def create_connection(db_file):
    try:
        conn = sqlite3.connect('capstone.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        print ("Opened database")
        return conn
    except Error as e:
        print(e)
        return None

#Table Creation

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

#issue with syntax of table creation - minor bug
def main():
    database = "capstone.db"
    
    sql_create_courses_table = """

    CREATE TABLE  if not exists courses(
       course_name TEXT,
       course_id INTEGER PRIMARY KEY,
       units INTEGER,
       department_id INTEGER,
       people_soft_id INTEGER,
       description TEXT,
       term_offered TEXT,
       CONSTRAINT ck_term CHECK(term_offered IN ('Autumn', 'Winter', 'Spring', 'Summer')),
       class_type text,
       CONSTRAINT ck_class CHECK(class_type IN ('In-Class', 'Online', 'Distance Learning', 'DL')),
       ); """

    sql_create_programs_table = """

    CREATE TABLE if not exists programs(
       program_id INTEGER PRIMARY KEY,
       program_name TEXT,
       course INTEGEER,
       FOREIGN KEY (course) REFERENCES courses(course_id)
       ); """

    sql_create_student_table = """

    CREATE TABLE if not exists students(
       student_id INTEGER PRIMARY KEY,
       first_name TEXT,
       last_name TEXT,
       status TEXT,
       CONSTRAINT ck_status CHECK(status IN ('Active', 'Graduated', 'Frozen')),
       term_start TEXT, 
       term_end TEXT,
       people_soft_id INTEGER,
       FOREIGN KEY (people_soft_id) references users(people_soft_id),
       dob DATE,
       phone INTEGER,
       email TEXT,
       address TEXT
       ); """

    sql_create_faculty_table = """

    CREATE TABLE if not exists faculty(
       faculty_id INTEGER PRIMARY KEY,
       people_soft_id INTEGER,
       FOREIGN KEY (people_soft_id) references users(people_soft_id),
       first_name TEXT,
       last_name TEXT,
       job_title TEXT
       ); """

    sql_create_users_table = """

    CREATE TABLE if not exists users(
       user_id INTEGER,
       password TEXT,
       people_soft_id INTEGER PRIMARY KEY NOT NULL,
       last_successful_login TEXT
       ); """
    
    #db connection
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_courses_table)
        create_table(conn, sql_create_programs_table)
        create_table(conn, sql_create_student_table)
        create_table(conn, sql_create_faculty_table)
        create_table(conn, sql_create_users_table)
    else:
        print("Did not create db connection.")


#run main
        if __name__ == '__main__':
            main()



    
