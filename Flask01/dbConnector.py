import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    passwd='Root@2022',
    database='databasename'
)

my_cursor = mydb.cursor()
# my_cursor.execute('Create database test02')
my_cursor.execute('show databases')
for db in my_cursor:
    print(db)
my_cursor.execute('use databasename')
print("my_cursor is ", my_cursor)
my_cursor.execute("insert into  testDB (PersonID, LastName, FirstName, Address, City) values ('107', 'LN5', 'FN5','address05', 'city5');")
# my_cursor.execute('select * from testDB')
# for db in my_cursor:
#     print(db)
mydb.commit()



