from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['HospitalDB']

# Initialize the admin collection
def initialize_admin():
    if db.admin.count_documents({}) == 0:
        db.admin.insert_one({'username': 'admin', 'password': '@dm1n'})
        print("Admin collection initialized with default values.")
    else:
        print("Admin collection already initialized.")

initialize_admin()

@app.route('/')
def home():
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    admin = db.admin.find_one({'username': username, 'password': password})
    if admin:
        session['username'] = username  # Store the username in the session
        return redirect(url_for('admin_home'))
    else:
        return "Invalid credentials", 401
#test
@app.route('/admin')
def admin_home():
    if 'username' in session:
        return render_template('Admin_Home_Page.html')
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session
    return redirect(url_for('home'))

@app.route('/AdminDocs')
def AdminDocs():
    if 'username' in session:
        return render_template('Admin_Manage_Doctors.html')
    else:
        return redirect(url_for('home'))

@app.route('/contact')
def contact():
    return "This is the contact page."

if __name__ == '__main__':
    app.run(debug=True)
