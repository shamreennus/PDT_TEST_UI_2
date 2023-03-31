import hashlib
import secrets
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

users = {
    'geeksforgeeks': {
        'password_hash': '3ce9ac522a58a64a0ecf7c1b35cb20d7c8826c128e6bf8c6b9ee0b0c73fa04a6',  # password is "123"
        'name': 'GeeksForGeeks',
    },
    'abdulkalam': {
        'password_hash': 'ee8e6a5d6c5a6b91de6a8f6b9d73fae232527a1f089e8ed2a2d38bce0ccf4641',  # password is "xyz"
        'name': 'Abdul Kalam',
    },
    'jony': {
        'password_hash': '29c0f7ea07e873abda11484e98b3a3d3de26dc60c1a3a99c31d8e23a1c36a69b',  # password is "abc"
        'name': 'Jony',
    },
    'tony': {
        'password_hash': 'f4bde4c6f15a6d5a6a5ee6f114940af14d0d3072fb73f5a06ba1b321c6967e45',  # password is "pqr"
        'name': 'Tony',
    },
}

def hash_password(password):
    """Hash the given password using SHA256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def validate_password(password, password_hash):
    """Check if the given password matches the given password hash."""
    return hash_password(password) == password_hash

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and validate_password(password, users[username]['password_hash']):
        session['username'] = username
        session['name'] = users[username]['name']
        return redirect(url_for('home'))
    else:
        return render_template('login.html', error='Invalid username or password')

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', name=session['name'])
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('name', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False, ssl_context='adhoc')