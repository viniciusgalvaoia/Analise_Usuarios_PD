# Drop Tables

courses_table_drop = "DROP TABLE IF EXISTS courses"
sessions_table_drop = "DROP TABLE IF EXISTS sessions"
student_follow_subject_table_drop = "DROP TABLE IF EXISTS student_follow_subject"
students_table_drop = "DROP TABLE IF EXISTS students"
subjects_table_drop = "DROP TABLE IF EXISTS subjects"
subscriptions_table_drop = "DROP TABLE IF EXISTS subscriptions"
universities_table_drop = "DROP TABLE IF EXISTS universities"


# Create Tables

courses_table_create =("""
    CREATE TABLE IF NOT EXISTS courses (
        Id INT,
        Name VARCHAR(100) NOT NULL
    );
""")

sessions_table_create = ("""
    CREATE TABLE IF NOT EXISTS sessions (
        StudentId VARCHAR(100),
        SessionStartTime DATETIME NOT NULL,
        StudentClient VARCHAR(20) NOT NULL
    );
""")

student_follow_subject_table_create = ("""
    CREATE TABLE IF NOT EXISTS student_follow_subject (
        StudentId VARCHAR(100),
        SubjectId INT NOT NULL,
        FollowDate DATETIME NOT NULL
    );
""")

students_table_create = ("""
    CREATE TABLE IF NOT EXISTS students (
        Id VARCHAR(100),
        RegisteredDate DATETIME NOT NULL,
        State VARCHAR(100),
        City VARCHAR(100),
        UniversityId INT,
        CourseId INT,
        SignupSource VARCHAR(20),
        StudentClient VARCHAR(100)
    );
""")

subjects_table_create = ("""
    CREATE TABLE IF NOT EXISTS subjects (
        Id INT,
        Name VARCHAR(300) NOT NULL
    );
""")

subscriptions_table_create = ("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        StudentId VARCHAR(100),
        PaymentDate DATETIME NOT NULL,
        PlanType VARCHAR(100) NOT NULL
    );
""")

universities_table_create = ("""
    CREATE TABLE IF NOT EXISTS universities (
        Id INT,
        Name VARCHAR(100) NOT NULL
    );
""")

# Insert Records

courses_table_insert = ("""
    INSERT INTO courses (Id, Name) 
    VALUES (%s, %s)
""")


sessions_table_insert = ("""
    INSERT INTO sessions (StudentId, SessionStartTime, StudentClient)
    VALUES(%s, %s, %s)
""")

student_follow_subject_table_insert = ("""
    INSERT INTO student_follow_subject (StudentId, SubjectId, FollowDate) 
    VALUES(%s, %s, %s) 
""")

students_table_insert = ("""
    INSERT INTO students (Id, RegisteredDate, State, City, UniversityId, CourseId, SignupSource, StudentClient) 
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s) 
""")

subjects_table_insert = ("""
    INSERT INTO subjects (Id, Name) 
    VALUES(%s, %s) 
""")

subscriptions_table_insert = ("""
    INSERT INTO subscriptions (StudentId, PaymentDate, PlanType) 
    VALUES(%s, %s, %s) 
""")

universities_table_insert = ("""
    INSERT INTO universities (Id, Name) 
    VALUES(%s, %s) 
""")

# QUERY LISTS

create_table_queries = [courses_table_create, 
                        sessions_table_create, 
                        student_follow_subject_table_create, 
                        students_table_create, 
                        subjects_table_create,
                        subscriptions_table_create,
                        universities_table_create]

drop_table_queries = [courses_table_drop, 
                      sessions_table_drop, 
                      student_follow_subject_table_drop, 
                      students_table_drop, 
                      subjects_table_drop,
                      subscriptions_table_drop,
                      universities_table_drop]