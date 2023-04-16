# SIHATE - Medical File Management System 🏥

Sihate is a medical file management system that enables efficient and secure management of patients, doctors, and medical files. The system comes with an authentication system that ensures that only authorized users can access the system.
# Folder structure
        .
        ├── sihate_core                    
        |   ├── asgi.py                    
        |   ├── wsgi.py                    
        |   ├── settings.py                    
        |   ├── urls.py                    
        ├── home_page                    
        ├── appointment                   
        ├── medical_records                   
        ├── users                   
        ├── media                     
        ├── static                   
        ├── templates                 
        |   ├── admin                
        |   ├── index                
        |   ├── profiles                
        ├── LICENSE
        └── README.md
# Features 💡

## Patient management🧍‍♂️:
 Add, update, and delete patient information.
## Doctor management: 
Add, update, and delete doctor information.
## Medical file management: 
Store and manage patient medical files securely.
## Appointment management:
Patients can request appointments with their doctors.
## Consultation management:
 Doctors can perform consultations with patients and provide prescriptions. The system stores the consultation information in the patient's medical file.
## Authentication system: 
Secure login for authorized users.
Statistics: The system provides statistics for common diabetes-related patient data.
# Installation

To install the system, follow the steps below:

Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt
Run the server using python manage.py runserver
Access the system through http://localhost:8000/ on your preferred web browser.
Usage

## Authentication 🔐
Before accessing the system, you need to log in using your username and password. The system comes with preloaded user accounts that you can use to log in.

## Patient Management 🧍‍♂️
To manage patients, click on the Patients link on the navigation bar. You can add, update, or delete patient information from this page.

## Doctor Management 👨‍⚕️
To manage doctors, click on the Doctors link on the navigation bar. You can add, update, or delete doctor information from this page.

## Medical File Management 🗃
To manage medical files, click on the Medical Files link on the navigation bar. You can view, add, or update medical files for each patient from this page.

## Appointment Management 🗓
To manage appointments, click on the Appointments link on the navigation bar. Patients can request appointments from this page, and doctors can approve or decline appointments.

## Consultation Management 🩺
To manage consultations, click on the Consultations link on the navigation bar. Doctors can perform consultations with patients, provide prescriptions, and store consultation information in the patient's medical file.

## Statistics 📊
To view statistics, click on the Statistics link on the navigation bar. The system provides statistics for common diabetes-related patient data.

# Conclusion

Sihate is an efficient and secure medical file management system that enables easy management of patients, doctors, medical files, appointments, consultations, and statistics. The system comes with an authentication system that ensures that only authorized users can access the system
Only manager can approve users Doctors & Patients.