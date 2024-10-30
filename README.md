# Mandatory Assignment 2024 - Information Systems

## Table of Contents

1. [Additional Assumptions Selected](#additional-assumptions-selected)
2. [Technologies Used](#technologies-used)
3. [File Descriptions](#file-descriptions)
4. [System Execution](#system-execution)
5. [System Usage](#system-usage)
6. [References](#references)

---

## Additional Assumptions Selected

- Users are categorized into three roles: Admin, Doctor, and Patient.
- Patients can only schedule appointments if a doctor is available.
- Appointment hours are between 09:00 and 16:00, with each appointment lasting one hour.
- Doctors and patients use the same login page to access the system.
- Patients can cancel their appointments but must confirm cancellation by entering the word "cancel."

## Technologies Used

- **Python 3.x**
- **Flask** for web server development
- **MongoDB** as the database
- **Docker** for containerization
- **HTML** for front-end structure
- **JavaScript** for front-end interactivity

## File Descriptions

- **app.py**: The main file for the Flask application, containing all backend routes and logic.
- **Dockerfile**: Defines how the Docker image for the Flask app is built.
- **docker-compose.yml**: Manages containers for the Flask app and MongoDB.
- **requirements.txt**: Lists all dependencies for the Flask app.
- **templates/**: Contains HTML files for the application's various pages.
  - **Login.html**: Login page for all users.
  - **Signup.html**: Signup page for patients.
  - **Admin_Home_Page.html**: Homepage for admin.
  - **Admin_Manage_Doctors.html**: Page for admin to manage doctors.
  - **Admin_Manage_Patients.html**: Page for admin to manage patients.
  - **Patient_Home_Page.html**: Homepage for patients.
  - **Doctor_Home_Page.html**: Homepage for doctors.
  - **Available_Doctors.html**: Page for selecting available doctors for appointments.
  - **Patient_View_Appointment.html**: Page to view appointment details.
  - **Patient_Setup_Appointment.html**: Page to schedule an appointment.
  - **Doctor_Change_Password.html**: Page for doctors to change passwords.

## System Execution

1. **Clone the repository:**
    ```bash
    git clone <repository URL>
    cd <repository directory name>
    ```

2. **Start the containers with Docker Compose:**
    ```bash
    docker-compose build
    docker-compose up
    ```

3. **Access the application:**
    Navigate to [http://localhost:5000](http://localhost:5000) in your web browser.

## System Usage

### For Admins:
- **Login**: Use the admin login page.<br/>
![Screenshot 2024-07-14 005335](https://github.com/user-attachments/assets/bf9002cf-35b6-4b12-ad2a-c8bc4c214aa9)
- **Manage Doctors**: Add, edit, or delete doctor profiles.<br/>
![Admin_Manage_Doctors](https://github.com/user-attachments/assets/2f2892dd-35c0-4cd9-a193-1d162327ec58)
- **Manage Patients**: Delete patient profiles.<br/>
![Admin_Manage_Patients](https://github.com/user-attachments/assets/cc13c40c-6795-4e74-acb3-93eee6dba46c)

### For Doctors:
- **Login**: Use the doctor login page.<br/>
![Screenshot 2024-07-14 005335](https://github.com/user-attachments/assets/b2c34714-bc1c-4696-b15f-1026d73b927c)
- **Manage Appointments**: View and manage your appointments.
- **Change Appointment Cost**: Update the cost of your services.<br/>
![Doctor_home_page](https://github.com/user-attachments/assets/e6c0567f-f076-491b-a734-2b64016e0679)
- **Change Password**: Update your account password.<br/>
![doctor_change_pass](https://github.com/user-attachments/assets/ad86e58f-85eb-4040-b668-8dd14c7a7921)

### For Patients:
- **Login**: Use the patient login page.<br/>
![Screenshot 2024-07-14 005335](https://github.com/user-attachments/assets/afee41c0-271f-4685-a84e-a29052e5312c)
- **Create Account**: Register a new account using the signup option.<br/>
![signup](https://github.com/user-attachments/assets/cd7f1d00-c5fa-4711-aa49-931d49e77a63)
- **Schedule Appointment**: Choose from available doctors and schedule appointments.<br/>
![Setup_Appointment](https://github.com/user-attachments/assets/e09a5c60-cb9d-4579-a234-b001bb0b09d3)
![available_doctors](https://github.com/user-attachments/assets/b56f8747-7471-4800-96e9-81dc78dc0c1b)
- **View Appointments**: View all scheduled appointments on the homepage.<br/>
![Patient_home](https://github.com/user-attachments/assets/da364d3b-9606-43b0-b878-229b8ee90374)
- **Cancel Appointment**: Cancel an appointment with confirmation.<br/>
![Patient_appointment](https://github.com/user-attachments/assets/d2ffb8b4-687f-4ecd-b865-2db9b07bc2c6)


## References

- Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- MongoDB Documentation: [https://docs.mongodb.com/](https://docs.mongodb.com/)
- Docker Documentation: [https://docs.docker.com/](https://docs.docker.com/)
- Jinja2 Templating: [https://jinja.palletsprojects.com/](https://jinja.palletsprojects.com/)
