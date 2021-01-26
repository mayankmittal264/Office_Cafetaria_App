# Office_Cafetaria_App
Problem Statement ---->
<---------------------------------------------------->
Create a form on the UI which captures :
Task 1. Fields for Data Capture (All fields are mandatory)
    Full Name
    Organization name
    Employee ID no.
    Mobile No.
    E-Mail
    Upload ID Card (Formats: png, jpeg)

Task 2. Provide a preview Screen which should :
    List all the fields as above.
    
Task 3. On Submission :
    Registration ID has to be generated and displayed on Success Screen.
    Store all the information captured in a local database
    Registration Date has to be generated as system date and get stored in Database.
<---------------------------------------------------->

How to Run ----->
<------------------------------------------------------>
Step 1. Run pip install -r requirements.txt
Step 2. Run Python manage.py makemigrations
Step 3. Run Python manage.py migrate
Step 4. Run Python manage.py runserver
Step 5. Open browser and type http://127.0.0.1:8000

To Get Admin access ->
Step 1. Run python manage.py createsuperuser
Step 2. Give username, emailid and password
Step 3. Go to browser and type  http://127.0.0.1:8000/admin/
Step 4. Login with your superuser credentials

<------------------------------------------------------>
