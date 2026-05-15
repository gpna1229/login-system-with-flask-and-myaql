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
#### Database Schema

The application uses a MySQL database with a single `users` table to manage membership data. 
If you don't have MySQL installed yet, you can download it from the [MySQL Official Downloads](https://dev.mysql.com/downloads/) page.

| Column Name | Data Type | Attributes | Description |
| :--- | :--- | :--- | :--- |
| **`id`** | `INT` | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each user. |
| **`username`** | `VARCHAR(50)` | NOT NULL, UNIQUE | The user's chosen display name (used for login). |
| **`password`** | `VARCHAR(255)` | NOT NULL | Hashed password for secure authentication. |
| **`email`** | `VARCHAR(100)` | NOT NULL, UNIQUE | The user's email address. |

You can initialize the database schema using the following SQL statement:

```sql
CREATE TABLE `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(50) NOT NULL UNIQUE,    
    `password` VARCHAR(255) NOT NULL,          
    `email` VARCHAR(100) NOT NULL UNIQUE,   
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 6. Running the Application
```bash
python app.py
```
