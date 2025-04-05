import pymysql

my = pymysql.connect(host="localhost", user="root", password="", database="Hello")

cur = my.cursor()

while True:
    try:
        delete_id=int(input("Enter the ID : "))
        break
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")
        
try:
    sql="delete from student where id=%s"

    cur.execute(sql,(delete_id,))

    my.commit()

    print("Data deleted successfully")

except Exception:
    print("Error")