
import cx_Oracle


#---------------------- Making connection to oracle server ------------------------


try:
   conn = cx_Oracle.connect("Dhruv/Mrdhruv123@//localhost:1521/orcl")
   print(conn.version)
except cx_Oracle.Error as e:
   print("Invalid connection details......")
   print(e)


#-------------------------- create cursor --------------------
try:
   cur = conn.cursor()
   print("Cursor connected successfully....")
except conn.Error as e:
    print("cursor not unable to connected..............")
    print(e)


# --------------------- create table -------------------   
# try:
#    cur.execute("""CREATE TABLE students
#                   (
#                      student_id NUMBER(4) PRIMARY KEY,
#                      name VARCHAR2(100),
#                      age NUMBER(3),
#                      gender VARCHAR2(10),
#                      subject VARCHAR2(100),
#                      marks NUMBER(10)
#                   )""")
#    print("Table is created successfully....")
# except cx_Oracle.Error as e:
#    print("Error:", e)


# -------------------------- Delete table ---------------------------
try:
   cur.execute("select * from students")
   print("Table is deleted ......")
except cx_Oracle.Error as e:
   print("Error....",e)


conn.commit()
cur.close()
conn.close()








