import flask
from flask import Flask, render_template, request, app
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/post")
def post():
    return render_template('post.html')

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    passwd='Root@2022'
)
@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        # fetch form data
        userdetails = request.form
        name = userdetails['nameDB']
        email = userdetails['emailDB']
        phoneNumber = userdetails['phoneDB']
        message = userdetails['messageDB']

        my_cursor = mydb.cursor()
        my_cursor.execute('use databasename')
        sql = "insert into  ContactMe (fullName, EmailAddress, PhoneNumber, message) values (%s,%s,%s,%s)"
        val = (name, email, phoneNumber, message)
        my_cursor.execute(sql, val)
        mydb.commit()
        my_cursor.close()
        return 'success'
    return render_template('submit.html')


if __name__ == '__main__':
    app.run(debug=True)

