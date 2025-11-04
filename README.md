# 🏫 School Management System (Django)

A full-featured **School Management Web App** built with **Django**, designed to manage both **students and teachers** efficiently.

---

## 🚀 Features

### 👨‍🎓 Student Features
- Secure **login** and **registration system**
- Personalized **dashboard**
- View and submit **assignments**
- View **grades** and **published results**

### 👩‍🏫 Teacher Features
- Secure **login** and **registration system**
- Dedicated **teacher dashboard**
- Create and upload **assignments**
- View and **grade student submissions**
- Publish **results** for students

---

## ⚙️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript (Bootstrap template)
- **Database:** SQLite (can be upgraded to PostgreSQL)
- **Version Control:** Git & GitHub

---

## 🧩 App Structure
school_management/
├── student/ # Handles student dashboard & submission logic
├── teacher/ # Handles teacher dashboard & grading system
├── templates/ # HTML templates for each user role
├── static/ # CSS, JS, and images
├── manage.py
└── requirements.txt


---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/school-management-system.git
   cd school-management-system

2. **Create a virtual environment**
    python -m venv venv
    source venv/Scripts/activate   # On Windows
    source venv/bin/activate       # On Mac/Linux

3. **Install dependencies**
    pip install -r requirements.txt

4. **Run migrations**
    python manage.py makemigrations
    python manage.py migrate

5. **Start the server**
    python manage.py runserver

6. **Access the app**
    Open your browser and visit:
    👉 http://127.0.0.1:8000/


## 📦 Future Improvements

- Add admin analytics dashboard
- Integrate PostgreSQL
- Implement email notifications
- Add file upload progress tracking


## ✨ Author

Iyendo Daniel Okeoghene (Seeker)
💻 Upcoming Software Engineer | Python & Django Developer
🌐 danieliyendo.netlify.app

⭐ If you like this project, please give it a star on GitHub!