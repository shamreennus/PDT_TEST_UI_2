# import all libraries
from flask import Flask, request, render_template

# initialize flask function
app = Flask(__name__)

# Make hello_world function
@app.route('/')
def hello_world():
    return render_template("Login.html")

# add database like login credentials,
# username and password
database = {'GeeksForGeeks': '123',
            'Abdul Kalam': 'xyz',
            'Jony': 'abc', 'Tony': 'pqr'}

# Make another function for login and we are
# making if and else condition for some
# situation like during wrong password wrong
# user and also for successful login
@app.route('/Form_login.html', methods=['POST', 'GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:
        return render_template('Login.html', name=name1, info='Invalid User ????!')
    else:
        if database[name1] != pwd:
            return render_template('Login.html', name=name1, info='Invalid Password ????!')
        else:            
            return render_template('Home.html', name=name1, info='Login successful!')


# Run flask in debug mode
if __name__ == '__main__':
    app.run()
