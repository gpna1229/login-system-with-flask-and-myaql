# Login System With Flask And MySQL
A simple project for a membership system built with Flask and MySQL, featuring registration, and an administrative member list view.

# Getting Started
Follow these steps to set up and run the project locally.
### 1. Prerequisites
This project requires **Python 3** and a running **MySQL** database instance.

### 2. Install Flask (A lightweight WSGI web application framework)
```bash
pip install Flask
```
### 3. Install Flask-SQLAlchemy (Simplifies SQLAlchemy integration with Flask)
```bash
pip install flask-sqlalchemy 
```
### 4. Install PyMySQL (A pure-Python MySQL client database driver)
```bash
pip install PyMySQL
```
### 5. Database Configuration
Before running the application, ensure you have configured your MySQL connection string in your settings.
```bash
DATABASE_URL=mysql+pymysql://username:password@host:port/database
```
### 6. Running the Application
```bash
python app.py
```
