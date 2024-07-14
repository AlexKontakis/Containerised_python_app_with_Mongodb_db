# Υποχρεωτική Εργασία 2024 Πληροφοριακών Συστημάτων

## Περιεχόμενα

1. [Επιπλέον Παραδοχές που Επιλέξατε](#επιπλέον-παραδοχές-που-επιλέξατε)
2. [Τεχνολογίες που Χρησιμοποιήθηκαν](#τεχνολογίες-που-χρησιμοποιήθηκαν)
3. [Περιγραφή των Αρχείων που κατασκευάσατε](#περιγραφή-των-αρχείων-που-κατασκευάσατε)
4. [Τρόπος Εκτέλεσης Συστήματος](#τρόπος-εκτέλεσης-συστήματος)
5. [Τρόπος Χρήσης του Συστήματος](#τρόπος-χρήσης-του-συστήματος)
6. [Αναφορές που χρησιμοποιήσατε](#αναφορές-που-χρησιμοποιήσατε)

## Επιπλέον Παραδοχές που Επιλέξατε

- Οι χρήστες του συστήματος διαχωρίζονται σε τρεις κατηγορίες: Admin, Doctor, και Patient.
- Οι ασθενείς μπορούν να προγραμματίζουν ραντεβού μόνο αν οι γιατροί είναι διαθέσιμοι.
- Ο χρόνος των ραντεβού είναι από 09:00 έως 16:00, και κάθε ραντεβού διαρκεί μία ώρα.
- Οι γιατροί και οι ασθενείς χρησιμοποιούν το ίδιο login page για να συνδεθούν στο σύστημα.
- Οι ασθενείς μπορούν να διαγράψουν ραντεβού τους, αλλά πρέπει να επιβεβαιώσουν τη διαγραφή με την εισαγωγή της λέξης "cancel".

## Τεχνολογίες που Χρησιμοποιήθηκαν

- **Python 3.x**
- **Flask** για την ανάπτυξη του web server
- **MongoDB** για τη βάση δεδομένων
- **Docker** για τη δημιουργία container
- **HTML** για το front-end
- **JavaScript** για διαδραστικότητα στο front-end

## Περιγραφή των Αρχείων που κατασκευάστηκαν

- **app.py**: Το κύριο αρχείο της εφαρμογής Flask, περιέχει όλες τις διαδρομές και τη λογική του backend.
- **Dockerfile**: Ορίζει τον τρόπο με τον οποίο θα κατασκευαστεί η εικόνα του Docker για το Flask app.
- **docker-compose.yml**: Περιέχει τη σύνθεση των containers για το Flask app και τη MongoDB.
- **requirements.txt**: Περιέχει όλες τις εξαρτήσεις που απαιτούνται για το Flask app.
- **templates/**: Περιέχει όλα τα HTML αρχεία για τις διάφορες σελίδες της εφαρμογής.
  - **Login.html**: Η σελίδα σύνδεσης για όλους τους χρήστες.
  - **Signup.html**: Η σελίδα εγγραφής για τους ασθενείς.
  - **Admin_Home_Page.html**: Η αρχική σελίδα του admin.
  - **Admin_Manage_Doctors.html**: Σελίδα διαχείρισης γιατρών από τον admin.
  - **Admin_Manage_Patients.html**: Σελίδα διαχείρισης ασθενών από τον admin.
  - **Patient_Home_Page.html**: Η αρχική σελίδα του ασθενή.
  - **Doctor_Home_Page.html**: Η αρχική σελίδα του γιατρού.
  - **Available_Doctors.html**: Σελίδα για την επιλογή διαθέσιμων γιατρών για ραντεβού.
  - **Patient_View_Appointment.html**: Σελίδα για την προβολή των λεπτομερειών ενός ραντεβού.
  - **Patient_Setup_Appointment.html**: Σελίδα για τoν προγραμματισμό ενός ραντεβού.
  - **Doctor_Change_Password.html**: Σελίδα για την αλλαγή κωδικού πρόσβασης.
    

## Τρόπος Εκτέλεσης Συστήματος

1. **Κλωνοποίηση του αποθετηρίου:**
    ```sh
    git clone <URL του αποθετηρίου>
    cd <όνομα καταλόγου αποθετηρίου>
    ```

2. **Εκκίνηση των containers με Docker Compose:**
    ```sh
    docker-compose build
    docker-compose up 
    ```

3. **Πρόσβαση στην εφαρμογή:**
    Η σελίδα γίνεται διαθέσιμη στο http://localhost:5000

## Τρόπος Χρήσης του Συστήματος

### Για τους Admins:
- **Σύνδεση**: Σύνδεση admin.<br/>
![Screenshot 2024-07-14 005335](https://github.com/user-attachments/assets/bf9002cf-35b6-4b12-ad2a-c8bc4c214aa9)
- **Διαχείριση Γιατρών**: Προσθήκη, επεξεργασία και διαγραφή γιατρών.<br/>
![Admin_Manage_Doctors](https://github.com/user-attachments/assets/2f2892dd-35c0-4cd9-a193-1d162327ec58)
- **Διαχείριση Ασθενών**: Διαγραφή ασθενών.<br/>
![Admin_Manage_Patients](https://github.com/user-attachments/assets/cc13c40c-6795-4e74-acb3-93eee6dba46c)

### Για τους Γιατρούς:
- **Σύνδεση**: Σύνδεση γιατρού.<br/>
![Screenshot 2024-07-14 005335](https://github.com/user-attachments/assets/b2c34714-bc1c-4696-b15f-1026d73b927c)
- **Διαχείριση Ραντεβού**: Προβολή των ραντεβού σας.
- **Αλλαγή Κόστους Ραντεβού**: Αλλαγή του κόστους των ραντεβού σας.<br/>
![Doctor_home_page](https://github.com/user-attachments/assets/e6c0567f-f076-491b-a734-2b64016e0679)
- **Αλλαγή Κωδικού**: Αλλαγή του κωδικού πρόσβασής σας.<br/>
![doctor_change_pass](https://github.com/user-attachments/assets/ad86e58f-85eb-4040-b668-8dd14c7a7921)

### Για τους Ασθενείς:
- **Σύνδεση**: Σύνδεση  ασθενή.<br/>
![Screenshot 2024-07-14 005335](https://github.com/user-attachments/assets/afee41c0-271f-4685-a84e-a29052e5312c)
- **Δημιουργία Λογαριασμού**: Στην σελίδα σύνδεσης, επιλέξτε την επιλογή εγγραφής για να δημιουργήσετε έναν νέο λογαριασμό ασθενή.<br/>
![signup](https://github.com/user-attachments/assets/cd7f1d00-c5fa-4711-aa49-931d49e77a63)
- **Προγραμματισμός Ραντεβού**: Επιλέξτε διαθέσιμους γιατρούς και προγραμματίστε ένα ραντεβού.<br/>
![Setup_Appointment](https://github.com/user-attachments/assets/e09a5c60-cb9d-4579-a234-b001bb0b09d3)
![available_doctors](https://github.com/user-attachments/assets/b56f8747-7471-4800-96e9-81dc78dc0c1b)
- **Προβολή Ραντεβού**: Προβολή όλων των ραντεβού σας στην αρχική σας σελίδα.<br/>
![Patient_home](https://github.com/user-attachments/assets/da364d3b-9606-43b0-b878-229b8ee90374)
- **Ακύρωση Ραντεβού**: Προβολή και ακύρωση ενός ραντεβού με επιβεβαίωση.<br/>
![Patient_appointment](https://github.com/user-attachments/assets/d2ffb8b4-687f-4ecd-b865-2db9b07bc2c6)


## Αναφορές που χρησιμοποιήθηκαν

- Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- MongoDB Documentation: [https://docs.mongodb.com/](https://docs.mongodb.com/)
- Docker Documentation: [https://docs.docker.com/](https://docs.docker.com/)
- Jinja2 Templating: [https://jinja.palletsprojects.com/](https://jinja.palletsprojects.com/)
