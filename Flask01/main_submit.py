from flask import Flask, render_template, request
import mysql.connector
import mysql


# app = Flask(__name__)

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    passwd='Root@2022'
)

@app.route('/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        #fetch the form data
        userDetails = request.form
        name = userDetails['namedb01']
        email = userDetails['emaildb01']
        phone = userDetails['mobiledb01']
        message = userDetails['messagedb01']

        my_cursor = mydb.cursor()
        my_cursor.execute('use databasename')
        sql = "insert into  ContactMe (fullName, EmailAddress, PhoneNumber, message) values (%s,%s,%s,%s)"
        val = (name, email, phone, message)
        my_cursor.execute(sql, val)
        mydb.commit()
        my_cursor.close()
        # return "success"
        print(name)
        print(email)
        print(phone)
        print(message)
        # return "success"
    return render_template('submit.html')

@app.route('/users')
def users():
    my_cursor = mydb.cursor()
    print("vvv")
    resultValue = my_cursor.execute('SELECT * FROM ContactMe')
    if resultValue > 0:
        userDetails = my_cursor.fetchall()
        print("userDetails", userDetails)
        return render_template('users.html', userDetails=userDetails)



# if __name__ == '__main__':
#     app.run(debug=True)



