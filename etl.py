import os
import glob
import mysql.connector
from mysql.connector import Error
import pandas as pd
from sql_queries import *

def process_courses_file(cur, filepath):
    """  
    - Read courses file.
    
    - Process courses data.
    
    - Insert data in courses table using courses_table_insert query.
    """
    # open courses file
    df = pd.read_json(filepath, orient='records')

    # insert courses record
    courses_data = df[['Id', 'Name']].values.tolist() 
    courses_data_rows = [tuple(rows) for rows in courses_data]
    cur.executemany(courses_table_insert, courses_data_rows)
    
    
def process_sessions_file(cur, filepath):
    """  
    - Read sessions file.
    
    - Process sessions data.
    
    - Insert data in sessions table using sessions_table_insert query.
    """
    # open courses file
    df = pd.read_json(filepath, orient='records')

    # insert courses record
    sessions_data = df[['StudentId', 'SessionStartTime', 'StudentClient']].values.tolist() 
    sessions_data_rows = [tuple(rows) for rows in sessions_data]
    cur.executemany(sessions_table_insert, sessions_data_rows)
    
    
def process_student_follow_subject_file(cur, filepath):
    """  
    - Read student_follow_subject file.
    
    - Process student_follow_subject data.
    
    - Insert data in sessions table using student_follow_subject_table_insert query.
    """
    # open courses file
    df = pd.read_json(filepath, orient='records')

    # insert courses record
    student_follow_subject_data = df[['StudentId', 'SubjectId', 'FollowDate']].values.tolist() 
    student_follow_subject_data_rows = [tuple(rows) for rows in student_follow_subject_data]
    cur.executemany(student_follow_subject_table_insert, student_follow_subject_data_rows)
    
    
def process_students_file(cur, filepath):
    """  
    - Read students file.
    
    - Process students data.
    
    - Insert data in sessions table using students_table_insert query.
    """
    # open courses file
    df = pd.read_json(filepath, orient='records')
    
    # convert NaN to None
    df = df.where(pd.notnull(df), None)

    # insert courses record
    students_data = df[['Id', 'RegisteredDate', 'State', 'City', 'UniversityId', 'CourseId', 'SignupSource', 'StudentClient']].values.tolist() 
    students_data_rows = [tuple(rows) for rows in students_data]
    cur.executemany(students_table_insert, students_data_rows)
    
    
def process_subjects_file(cur, filepath):
    """  
    - Read subjects file.
    
    - Process subjects data.
    
    - Insert data in sessions table using subjects_table_insert query.
    """
    # open courses file
    df = pd.read_json(filepath, orient='records')

    # insert courses record
    subjects_data = df[['Id', 'Name']].values.tolist() 
    subjects_data_rows = [tuple(rows) for rows in subjects_data]
    cur.executemany(subjects_table_insert, subjects_data_rows)
    
    
def process_subscriptions_file(cur, filepath):
    """  
    - Read subscriptions file.
    
    - Process subscriptions data.
    
    - Insert data in sessions table using subscriptions_table_insert query.
    """
    # open courses file
    df = pd.read_json(filepath, orient='records')

    # insert courses record
    subscriptions_data = df[['StudentId', 'PaymentDate', 'PlanType']].values.tolist()
    subscriptions_data_rows = [tuple(rows) for rows in subscriptions_data]
    cur.executemany(subscriptions_table_insert, subscriptions_data_rows)    


def process_universities_file(cur, filepath):
    """  
    - Read universities file.
    
    - Process universities data.
    
    - Insert data in sessions table using universities_table_insert query.
    """
    # open courses file
    df = pd.read_json(filepath, orient='records')
    # open courses file
    df = pd.read_json(filepath, orient='records')

    # insert courses record
    universities_data = df[['Id', 'Name']].values.tolist()
    universities_data_rows = [tuple(rows) for rows in universities_data]
    cur.executemany(universities_table_insert, universities_data_rows)
    
    
def process_data(cur, conn, filepath, func):   
    """  
    iterate over files and process.
    """
    for datafile, func in zip(filepath, func):
        func(cur, datafile)
        conn.commit()


def main():
    """  
    - Establishes connection with the passeidireto database and gets
    cursor to it.  
    
    - Process and insert data in all tables.  
    
    - Finally, closes the connection. 
    """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='passeidiretodb',
                                       user='root',
                                       password='admin')
        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cur = conn.cursor()
            cur.execute("select database();")
            record = cur.fetchone()
            print("You're connected to database: ", record)
            cur.execute("SET GLOBAL max_allowed_packet=1073741824;")

    except Error as e:
        print("Error while connecting to MySQL", e)
    
    filepath_list = ['data/BASE_A/courses.json',
                     'data/BASE_A/sessions.json',
                     'data/BASE_A/student_follow_subject.json',
                     'data/BASE_A/students.json',
                     'data/BASE_A/subjects.json',
                     'data/BASE_A/subscriptions.json',
                     'data/BASE_A/universities.json']
    
    func_list = [process_courses_file, 
                 process_sessions_file, 
                 process_student_follow_subject_file, 
                 process_students_file,
                 process_subjects_file, 
                 process_subscriptions_file, 
                 process_universities_file]
    
    process_data(cur, conn, filepath=filepath_list, func=func_list)
    conn.close()
    print("MySQL connection is closed")

if __name__ == "__main__":
    main()