from numpy import NAN
import pandas as pd
import cx_Oracle
 

df = pd.read_excel("book_table.xlsx").replace(NAN,None)
print(df)
#create table
def create_table(sql):

    try:
        #create connection
        conn = cx_Oracle.connect("Dhruv/Mrdhruv123@//localhost:1521/orcl")
    except cx_Oracle.Error as e:
        print("Connection fail....",e)
    else:
        print("Connection created succesfully........")
        #create cursor
        try:
           cur = conn.cursor()
        except cx_Oracle.Error as e:
            print("cursor not created....",e)
        else:
            print("cursor created ....")
            try:
                 #create table
                 cur.execute(sql)
            except cx_Oracle.Error as e:
                print("Table is not created.....",e)
            else:
                print("Table created succesfully...")
                conn.commit()
    finally:
        cur.close()
        conn.close()
        

#insert data function
def insert_data(data):
    try:
        #create connection
        conn = cx_Oracle.connect("Dhruv/Mrdhruv123@//localhost:1521/orcl")
    except cx_Oracle.Error as e:
        print("Connection fail....",e)
    else:
        print("Connection created succesfully........")
        #create cursor
        try:
           cur = conn.cursor()
        except cx_Oracle.Error as e:
            print("cursor not created....",e)
        else:
            print("cursor created ....")
            try:
                #insert data
                sql = """INSERT INTO book VALUES(:1,:2,:3,:4,:5,:6)"""
                cur.executemany(sql,data)
            except cx_Oracle.Error as e:
                print("Data is not inserted.....",e)
            else:
                print("Data is inserted  succesfully...")
                conn.commit()
    finally:
        cur.close()
        conn.close()


#fetch all data
def fetchall():
    try:
        #create connection
        conn = cx_Oracle.connect("Dhruv/Mrdhruv123@//localhost:1521/orcl")
    except cx_Oracle.Error as e:
        print("Connection fail....",e)
    else:
        print("Connection created succesfully........")
        #create cursor
        try:
           cur = conn.cursor()
        except cx_Oracle.Error as e:
            print("cursor not created....",e)
        else:
            print("cursor created ....")
            try:
                #insert data
                sql = """SELECT * FROM Book"""
                cur.execute(sql)
                data = cur.fetchall()
            except cx_Oracle.Error as e:
                print("Data is not fetch.....",e)
            else:
                print("Data is fetch succesfully...")
                conn.commit()
                return data
    finally:
        cur.close()
        conn.close()

#create table quary 
create_table( """
    CREATE TABLE Book(
    Title VARCHAR2(400) NOT NULL,
    Author VARCHAR2(300) NOT NULL,
    Publisher VARCHAR2(300),
    Year NUMBER(4) CHECK(LENGTH(Year)=4),
    Pages NUMBER(6),
    Price NUMBER(6)
    )""")


#insert data
insert_data([tuple(v[1]) for v in df.iterrows()])

#fetchall data
# data = fetchall()
# print(pd.DataFrame(data, columns=["Title","Author","Publisher","Year","Pages","Price"]))
   

