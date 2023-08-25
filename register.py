#!C:\Python311\python.exe
import cgi
import mysql.connector
print("content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")

print("<h1>Welcome</h1>")
form=cgi.FieldStorage()
fname=form.getvalue("name")
fMobile=form.getvalue("mobile")
fEmail=form.getvalue("email")
fPassword=form.getvalue("password")
print("<h1>",fname,fMobile,fEmail,fPassword,"<h1>")
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="institute")
mycursor=mydb.cursor();
sql="INSERT INTO student(name,Mobile,Email,Password) VALUES(%s,%s,%s,%s)"
val=(fname,fMobile,fEmail,fPassword)
mycursor.execute(sql,val)
mydb.commit()

print("</body>")
print("</html>")
