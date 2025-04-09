import pymysql

my=pymysql.connect(host="localhost",user="root",password="",database="Hello")

cur=my.cursor()
print("{:<15}{:<15}{:<15}".format("ID","Name","Surename"))

try:
    sql="select student.id,student.name,result.surnameame from student,result where student.id=result.id"

    cur.execute(sql)

    data=cur.fetchall()

    for i in data:
        print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

except :
    print("Error")      