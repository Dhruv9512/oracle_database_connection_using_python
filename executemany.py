import cx_Oracle

def insert_data(sql):
#------------------------- connection --------------------
    try:
       conn = cx_Oracle.connect("Dhruv/Mrdhruv123@//localhost:1521/orcl")
    except cx_Oracle.Error as error :
        print("Connection fail... ",error)
    else:
        print("Connection created ........")
        # ------------------------ cursor --------------------------
        try:
            cur = conn.cursor()

            # ------------ Insert single data Normaly -------------
            # cur.execute(sql)
            # print("Data is inserted succesfully....")


            # ------------ Insert single data Using list -------------
            # temp = "INSERT INTO Players VALUES (:1,:2,:3,:4,:5)"
            # cur.execute(temp,sql)


            # -------------- Insert multiple values -----------
            temp = "INSERT INTO Players VALUES (:1,:2,:3,:4,:5)"
            cur.executemany(temp,sql)
        except cx_Oracle.Error as error:
            conn.rollback()
            cur.close()
            print("Data is not inserted created.....",error)
        else:
            print("Data is inserted succesfully....")                       
            conn.commit()
    finally:
        conn.close()


# -------------------- Insert single data ---------------------
# insert_data("""
# INSERT INTO Players VALUES(1,'Dhruv','csk','N','Y')
# """)



# ------------ Insert single data Using list -------------
# insert_data([2,'Riya','MI','Y','N'])


# -------------- Insert multiple values -----------
data = [(3,'Priya','KKR','N','Y'),(4,'vishal','RCB','Y','N')]
insert_data(data)