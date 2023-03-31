# import all libraries
import hashlib
import secrets
from flask import Flask, request, render_template

# initialize flask function
app = Flask(__name__)

# Make hello_world function
@app.route('/')
def hello_world():
    return render_template("Login.html")


app.secret_key = secrets.token_urlsafe(16)


# define the database
database = {
    'geeks': {
        'password_hash': hashlib.sha256('123'.encode()).hexdigest(),
        'name': 'Geeks',
    },
    'abdulkalam': {
        'password_hash': hashlib.sha256('xyz'.encode()).hexdigest(),
        'name': 'Abdul Kalam',
    },
    'jony': {
        'password_hash': hashlib.sha256('abc'.encode()).hexdigest(),
        'name': 'Jony',
    },
    'tony': {
        'password_hash': hashlib.sha256('pqr'.encode()).hexdigest(),
        'name': 'Tony',
    },
}

def hash_password(password):
    """Hash the given password using SHA256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def validate_password(password, password_hash):
    """Check if the given password matches the given password hash."""
    return password_hash == hash_password(password)


# Make another function for login and we are
# making if and else condition for some
# situation like during wrong password wrong
# user and also for successful login
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
        if hashlib.sha256(pwd.encode()).hexdigest() != database[name1]['password_hash']:
            return render_template('Login.html', name=name1, info='Invalid Password ????!')
        else:            
            return render_template('Home.html', name=name1, info='Login successful!')


# Run flask in debug mode
if __name__ == '__main__':
    app.run(debug=False)
