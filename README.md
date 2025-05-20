📧 Django Real-time Email OTP Verification
This project implements real-time OTP (One-Time Password) email verification using Django. It allows users to verify their email addresses by sending a 6-digit OTP to their inbox and validating it before proceeding.

![Screenshot (88)](https://github.com/user-attachments/assets/b3745299-d9bc-4a59-933a-e749e2d9710d)


🚀 Features
User registration and login (optional)

Send OTP to email in real-time

OTP expiry (default: 5 minutes)

OTP retry logic

OTP verification endpoint

Secure and extendable codebase

Email console backend (for development)

Ready for SMTP email backend (for production)

🛠️ Tech Stack
Backend: Django (Python)

Database: SQLite (default), easily switchable

Email: Django Email Backend (SMTP or Console)

Others: Python random, Django models & forms

📂 Project Structure

OTP_project/
├── emailotp/
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── otp_project/
│   ├── asgi.py
│   ├── wsgi.py
│   ├── settings.py
│   └── urls.py
├── otp-frontend/
│   ├── src
│       ├── App.css
│       ├── App.js
│       ├── index.js
│       ├── index.css
├── manage.py

🔧 Setup Instructions
1. Clone the Repository
git clone https://github.com/yourusername/Email_otp.git
cd Email_otp

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Requirements
pip install -r requirements.txt

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Run the Server
python manage.py runserver

🧪 Usage Flow
User enters email and submits.

Django sends a 6-digit OTP to the provided email.

User enters the OTP in a verification form.

OTP is validated, and email is marked as verified.

🧰 Configuration
SMTP Email Setup (for production):
In settings.py:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'


For development, use:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
   

