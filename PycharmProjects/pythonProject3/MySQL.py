import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="management"
)
dbcursor = db.cursor()



dbcursor.execute("select * from employee")
for x in dbcursor:
    print(x)


sql = "insert into employee (name, address) values (%s, %s)"
value = ("John", "Highway 21")

dbcursor.execute("insert into employee (name, Emp_id) values ('John', 12)")

db.commit()

print(dbcursor.column_names, "employee")
dbcursor.execute("select * from employee")
for x in dbcursor:
    print(x)
