from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from bson.objectid import ObjectId

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

@app.route('/admin/doctors')
def manage_doctors():
    if 'username' in session:
        doctors = db.doctors.find()
        return render_template('Admin_Manage_Doctors.html', doctors=doctors, action='Add')
    else:
        return redirect(url_for('home'))

@app.route('/admin/doctors/add', methods=['POST'])
def add_doctor():
    if 'username' not in session:
        return redirect(url_for('home'))

    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    appointment_cost = float(request.form['appointment_cost'])
    specialization = request.form['specialization']

    if not email.endswith('@gmail.com'):
        return "Email must end with @gmail.com", 400

    db.doctors.insert_one({
        'name': name,
        'last_name': last_name,
        'email': email,
        'username': username,
        'password': password,
        'appointment_cost': appointment_cost,
        'specialization': specialization
    })
    return redirect(url_for('manage_doctors'))

@app.route('/admin/doctors/edit/<id>', methods=['POST'])
def edit_doctor(id):
    if 'username' not in session:
        return redirect(url_for('home'))

    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    appointment_cost = float(request.form['appointment_cost'])
    specialization = request.form['specialization']

    if not email.endswith('@gmail.com'):
        return "Email must end with @gmail.com", 400

    db.doctors.update_one(
        {'_id': ObjectId(id)},
        {'$set': {
            'name': name,
            'last_name': last_name,
            'email': email,
            'username': username,
            'password': password,
            'appointment_cost': appointment_cost,
            'specialization': specialization
        }}
    )
    return redirect(url_for('manage_doctors'))

@app.route('/admin/doctors/delete/<id>')
def delete_doctor(id):
    if 'username' not in session:
        return redirect(url_for('home'))

    db.doctors.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('manage_doctors'))

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/contact')
def contact():
    return "This is the contact page."

if __name__ == '__main__':
    app.run(debug=True)
