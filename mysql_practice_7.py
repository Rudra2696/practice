import pymysql

my = pymysql.connect(host="localhost", user="root", password="", database="Hello")

cur = my.cursor()

delete_id=int(input("Enter the ID : "))

try:
    sql="delete from student where id=%s"

    cur.execute(sql,(delete_id,))

    my.commit()

    print("Data deleted successfully")

except Exception:
    print("Error")