import mysql.connector
from mysql.connector import Error
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Creates and connects to the passeidiretodb
    - Returns the connection and cursor to passeidiretodb
    """
    
    # connect to default database
    try:  
        conn = mysql.connector.connect(host='localhost',
                                       database='sys',
                                       user='root',
                                       password='admin')
    
        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cur = conn.cursor()
            cur.execute("select database();")
            record = cur.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS passeidiretodb")
    cur.execute("CREATE DATABASE passeidiretodb") #WITH ENCODING 'utf8' TEMPLATE template0
    
    # close connection to default database
    #cursor.close()
    conn.close()
    print("MySQL connection is closed")

    # close connection to default database
    conn.close()  
    
    # connect to passeidireto database
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

    except Error as e:
        print("Error while connecting to MySQL", e)
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the passeidireto database. 
    
    - Establishes connection with the passeidireto database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()
    print("MySQL connection is closed")


if __name__ == "__main__":
    main()