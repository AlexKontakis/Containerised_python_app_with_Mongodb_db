from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

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
    
    # Check for admin login
    admin = db.admin.find_one({'username': username, 'password': password})
    if admin:
        session['username'] = username  # Store the username in the session
        return redirect(url_for('admin_home'))
    
    # Check for patient login
    patient = db.patients.find_one({'username': username, 'password': password})
    if patient:
        session['patient_username'] = username  # Store the patient username in the session
        session['patient_name'] = patient['name']
        session['patient_last_name'] = patient['last_name']
        return redirect(url_for('patient_home'))
    
    doctor = db.doctors.find_one({'username': username, 'password': password})
    if doctor:
        session['doctor_username'] = username
        session['doctor_name'] = doctor['name']
        session['doctor_last_name'] = doctor['last_name']
        return redirect(url_for('doctor_home'))
    return "Invalid credentials", 401

@app.route('/admin')
def admin_home():
    if 'username' in session:
        return render_template('Admin_Home_Page.html')
    else:
        return redirect(url_for('home'))

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)  # Remove the username from the session
    session.pop('patient_username', None)  # Remove the patient username from the session
    session.pop('patient_name', None)  # Remove the patient name from the session
    session.pop('patient_last_name', None)  # Remove the patient last name from the session
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

@app.route('/admin/doctors/delete/<id>', methods=['POST'])
def delete_doctor(id):
    if 'username' not in session:
        return redirect(url_for('home'))

    db.doctors.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('manage_doctors'))

@app.route('/admin/patients')
def manage_patients():
    if 'username' in session:
        patients = db.patients.find()
        return render_template('Admin_Manage_Patients.html', patients=patients, action='Add')
    else:
        return redirect(url_for('home'))

@app.route('/admin/patients/add', methods=['POST'])
def add_patient():
    if 'username' not in session:
        return redirect(url_for('home'))

    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    ssn = int(request.form['ssn'])
    dob = request.form['dob']
    username = request.form['username']
    password = request.form['password']

    if not email.endswith('@gmail.com'):
        return "Email must end with @gmail.com", 400

    db.patients.insert_one({
        'name': name,
        'last_name': last_name,
        'email': email,
        'ssn': ssn,
        'dob': datetime.datetime.strptime(dob, '%Y-%m-%d'),
        'username': username,
        'password': password
    })
    return redirect(url_for('manage_patients'))

@app.route('/admin/patients/edit/<id>', methods=['POST'])
def edit_patient(id):
    if 'username' not in session:
        return redirect(url_for('home'))

    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    ssn = int(request.form['ssn'])
    dob = request.form['dob']
    username = request.form['username']
    password = request.form['password']

    if not email.endswith('@gmail.com'):
        return "Email must end with @gmail.com", 400

    db.patients.update_one(
        {'_id': ObjectId(id)},
        {'$set': {
            'name': name,
            'last_name': last_name,
            'email': email,
            'ssn': ssn,
            'dob': datetime.datetime.strptime(dob, '%Y-%m-%d'),
            'username': username,
            'password': password
        }}
    )
    return redirect(url_for('manage_patients'))

@app.route('/admin/patients/delete/<id>', methods=['POST'])
def delete_patient(id):
    if 'username' not in session:
        return redirect(url_for('home'))

    db.patients.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('manage_patients'))

@app.route('/signup')
def signup_form():
    return render_template('Signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    ssn = int(request.form['ssn'])
    dob = request.form['dob']
    username = request.form['username']
    password = request.form['password']

    if not email.endswith('@gmail.com'):
        return "Email must end with @gmail.com", 400

    db.patients.insert_one({
        'name': name,
        'last_name': last_name,
        'email': email,
        'ssn': ssn,
        'dob': datetime.datetime.strptime(dob, '%Y-%m-%d'),
        'username': username,
        'password': password
    })
    return redirect(url_for('home'))

@app.route('/doctor')
def doctor_home():
    if 'doctor_username' in session:
        doctor_username = session['doctor_username']
        doctor_name = session['doctor_name']

        appointments = db.appointments.find({'doctor_username': doctor_username})

        return render_template('Doctor_Home_Page.html', doctor_name=doctor_name, appointments=appointments)
    
@app.route('/doctor/change_cost', methods=['POST'])
def change_cost():
    if 'doctor_username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        new_cost = float(request.form.get('new_cost'))
        
        if new_cost < 0:
            flash("Cost must be a positive number.", 'error')
            return redirect(url_for('doctor_home'))

        doctor_username = session['doctor_username']
        db.appointments.update_many({'doctor_username': doctor_username}, {'$set': {'cost': new_cost}})
        
        flash("Appointment cost changed successfully!", 'success')
        return redirect(url_for('doctor_home'))

    return redirect(url_for('doctor_home'))
    
@app.route('/doctor/change_password', methods=['GET', 'POST'])
def change_password():
    if 'doctor_username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if new_password != confirm_password:
            flash("Passwords do not match. Please try again.", 'error')
            return redirect(url_for('change_password'))

        doctor_username = session['doctor_username']
        doctor = db.doctors.find_one({'username': doctor_username})

        if doctor and doctor['password'] == new_password:
            flash("New password cannot be the same as the current password. Please choose a different password.", 'error')
            return redirect(url_for('change_password'))

        db.doctors.update_one({'username': doctor_username}, {'$set': {'password': new_password}})
        
        flash("Password changed successfully!", 'success')
        return redirect(url_for('doctor_home'))

    return render_template('Doctor_Change_Password.html')
@app.route('/patient')
def patient_home():
    if 'patient_username' in session:
        patient_username = session['patient_username']
        patient_name = session['patient_name']
        
        # Fetch all appointments for the logged-in patient
        appointments = db.appointments.find({'patient_username': patient_username})
        
        return render_template('Patient_Home_Page.html', patient_name=patient_name, appointments=appointments)
    else:
        return redirect(url_for('home'))

@app.route('/patient/appointments')
def setup_appointment_form():
    if 'patient_username' in session:
        return render_template('Patient_Setup_Appointment.html')
    else:
        return redirect(url_for('home'))

@app.route('/patient/appointments/available-doctors', methods=['POST'])
def available_doctors():
    if 'patient_username' not in session:
        return redirect(url_for('home'))

    specialization = request.form['specialization']
    date = request.form['date']
    time = request.form['time']

    # Convert time to integer
    hour = int(time.split(':')[0])

    # Calculate end time for the appointment
    end_time = (hour + 1) % 24

    # Fetch all doctors with the specified specialization
    doctors = db.doctors.find({'specialization': specialization})

    # Fetch existing appointments for the specified date and time
    existing_appointments = db.appointments.find({
        'date': datetime.datetime.strptime(date, '%Y-%m-%d'),
        '$or': [
            {'time': time},
            {'time': str(end_time) + ':00'}
        ]
    })

    # Filter out doctors who have appointments at the specified time
    available_doctors = [doctor for doctor in doctors if doctor['username'] not in [appointment['doctor_username'] for appointment in existing_appointments]]

    return render_template('Available_Doctors.html', doctors=available_doctors, date=date, time=time)

@app.route('/patient/appointments/add', methods=['POST'])
def add_appointment():
    if 'patient_username' not in session:
        return redirect(url_for('home'))

    doctor_id = request.form['doctor']
    date = request.form['date']
    time = request.form['time']
    reason = request.form['reason']

    patient = db.patients.find_one({'username': session['patient_username']})
    doctor = db.doctors.find_one({'_id': ObjectId(doctor_id)})

    appointment = {
        'patient_name': patient['name'],
        'patient_last_name': patient['last_name'],
        'doctor_name': doctor['name'],
        'doctor_last_name': doctor['last_name'],
        'date': datetime.datetime.strptime(date, '%Y-%m-%d'),
        'time': time,
        'cost': doctor['appointment_cost'],
        'reason': reason,
        'specialization': doctor['specialization'],
        'doctor_username': doctor['username'],
        'patient_username': patient['username']
    }

    db.appointments.insert_one(appointment)
    return redirect(url_for('patient_home'))
@app.route('/patient/appointments/view/<appointment_id>', methods=['GET'])
def view_appointment(appointment_id):
    if 'patient_username' not in session:
        return redirect(url_for('home'))

    appointment = db.appointments.find_one({'_id': ObjectId(appointment_id)})
    if not appointment:
        return "Appointment not found", 404

    return render_template('Patient_View_Appointment.html', appointment=appointment)




@app.route('/patient/appointments/cancel/<appointment_id>', methods=['POST'])
def cancel_appointment(appointment_id):
    if 'patient_username' not in session:
        return redirect(url_for('home'))

    db.appointments.delete_one({'_id': ObjectId(appointment_id)})

    return redirect(url_for('patient_home'))


if __name__ == '__main__':
    app.run(debug=True)