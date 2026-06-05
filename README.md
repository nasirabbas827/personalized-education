# personalized_education  

A lightweight Django‑based web application that delivers personalized learning experiences through adaptive quizzes, custom curricula, and real‑time feedback. The project is structured for easy extension, testing, and deployment.

---  

## Overview  

`personalized_education` provides a modular platform where educators can create, manage, and deliver tailored educational content. Core functionalities include:

* Adaptive quizzes that adjust difficulty based on learner performance.  
* Dynamic curriculum generation driven by user profiles.  
* Administrative interface for managing courses, questions, and analytics.  

The codebase follows Django best practices, separating concerns into the `education` project settings and the `myapp` application that houses the domain logic.

---  

## Features  

| ✅ | Feature |
|---|---|
| 📚 | **Curriculum Management** – Create and edit courses, modules, and lessons. |
| 🧩 | **Adaptive Quiz Engine** – Questions are selected based on prior answers. |
| 📊 | **Analytics Dashboard** – View student progress, scores, and engagement metrics. |
| 👩‍🏫 | **Admin Panel** – Full CRUD for all models via Django’s built‑in admin. |
| 🧪 | **Test Suite** – Unit tests for models, forms, and views (`myapp/tests.py`). |
| 🔧 | **Extensible Architecture** – Clear separation between project settings and app logic. |

---  

## Tech Stack  

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3.9, Django 4.x |
| **Frontend** | HTML5, CSS3 (Bootstrap optional) |
| **Database** | SQLite (default) – can be swapped for PostgreSQL, MySQL, etc. |
| **Server** | WSGI (`education/wsgi.py`) / ASGI (`education/asgi.py`) |
| **Testing** | Django’s test framework (`myapp/tests.py`) |
| **Version Control** | Git (GitHub) |

---  

## Installation  

> **Prerequisite:** Python 3.9+ and `git` installed on your machine.

```bash
# 1. Clone the repository
git clone https://github.com/your-username/personalized_education.git
cd personalized_education

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install --upgrade pip
pip install django  # Or use a requirements.txt if added later

# 4. Apply database migrations
python manage.py migrate

# 5. (Optional) Create a superuser for the admin interface
python manage.py createsuperuser
```

---  

## Usage  

```bash
# Start the development server
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/` to explore the application.

* **Admin panel:** `http://127.0.0.1:8000/admin/` (login with the superuser created above).  
* **App URLs:** Defined in `myapp/urls.py` and included in `education/urls.py`.  

### Running Tests  

```bash
python manage.py test myapp
```

### Deploying to Production  

1. Set `DEBUG = False` in `education/settings.py`.  
2. Configure a production‑ready database (PostgreSQL recommended).  
3. Use a WSGI server such as **Gunicorn** or an ASGI server like **Uvicorn** for async support.  
4. Add any required environment variables (e.g., `SECRET_KEY`, `DATABASE