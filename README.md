# ToDosApp

A clean and minimal Django-based To-Do list web application for managing daily tasks with CRUD functionality.

## Overview

**ToDosApp** is a simple productivity tool built with Django. It allows users to create, edit, and delete to-do items through an intuitive web interface. The app is ideal for learning Django fundamentals and practicing full-stack development workflows.

## Features

- Create, update, and delete tasks
- View all tasks in a clean dashboard
- Modular structure with reusable templates
- Error handling with custom 404 page
- Lightweight and responsive UI using Bootstrap

## Technologies Used

- Python 3.11+
- Django 5.x
- SQLite (default)
- HTML5 / CSS3 / Bootstrap

## Project Structure

ToDosProject/ ├── main/                  # Main Django settings and configurations ├── tasks/                 # Django app for task handling │   ├── models.py          # Task model │   ├── views.py           # Task views │   ├── forms.py           # Django forms for tasks │   ├── templates/         # HTML templates │   └── urls.py            # URL patterns for the app ├── db.sqlite3             # Default SQLite database ├── manage.py              # Django project runner └── README.md              # Project documentation

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/shehablotfallah/ToDosApp.git
cd ToDosApp
```
2. Set Up a Virtual Environment

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies

If you have a requirements.txt:

pip install -r requirements.txt

If not:
```bash
pip install django
````
4. Run the Server
```bash
python manage.py runserver
```
Visit: http://127.0.0.1:8000/

Screenshots



![Screenshot 2025-04-18 010254](https://github.com/user-attachments/assets/a1695a57-c48a-436d-9592-ebf751051d2f)


Future Improvements

User authentication & sessions

Due dates and reminders

Task filtering & categories

RESTful API integration


License

This project is licensed under the [MIT License](https://github.com/shehablotfallah/ToDosApp?tab=MIT-1-ov-file).


---

Author

Developed by [Shehab Lotfallah](https://github.com/shehablotfallah)
