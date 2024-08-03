import cx_Oracle

def fetch_data(N):

    # ------------------- create connection ------------------
    try:
        conn = cx_Oracle.connect("Dhruv/Mrdhruv123@//localhost:1521/orcl")
    except cx_Oracle.Error as error:
        print("Connection Not created......",error)
    else:
        print("Connection created succesfully........")
        
        try:
        #----------------------- Create cursor --------------------
           cur = conn.cursor()
        except cx_Oracle.Error as error:
            print("Cursor not created......",error)
        else:
            print("Cursor created succesfully.......")

            
            try:
                cur.execute("SELECT * FROM Players")
                #---------------- fetch singl row --------------
                # data = cur.fetchone()


                #---------------- featch all row --------------
                # data = cur.fetchall()

                #---------------- featch N number of row --------------
                data = cur.fetchmany(N)

            except cx_Oracle.Error as error:
                print("Not featched......",error)
                conn.rollback()
            else:
                return data
            finally:
                cur.close()
    finally:
        conn.close()


#---------------- featch singl row --------------
# print(fetch_data())


#---------------- featch all row --------------
# for i,v in enumerate(fetch_data()):
#     print("Index ",i," : ",v)


#---------------- featch N number of row --------------
for i,v in enumerate(fetch_data(int(input("Enter Number of rows that you want to fetch:- ")))):
    print("Index ",i," : ",v)