import pymysql

my=pymysql.connect(host="localhost",user="root",password="",database="Hello")

cur=my.cursor()

try:
    t="insert into student(name,marks) values(%s,%s)"

    ins=[("Rohit",78) , ("Shubham",79) , ("Rajesh",80)]
    cur.executemany(t,ins)

    my.commit()

    print("Data inserted successfully")
except :
    print("Error")   