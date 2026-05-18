# Login System With Flask And MySQL
A simple project for a membership system built with Flask and MySQL, featuring registration, and an administrative member list view.

## Tech Stack
* **Backend**: Python, Flask, Flask-SQLAlchemy
* **Frontend**: Tailwind CSS (UI designed in collaboration with Google Gemini)
* **Database**: MySQL
* **Deployment**: AWS EC2 (Ubuntu), OpenSSH, Git

## Getting Started
Follow these steps to set up and run the project locally.
### 1. Prerequisites
This project requires **Python 3** and a running **MySQL** database instance.

### 2. Clone This Project
```bash
git clone https://github.com/gpna1229/login-system-with-flask-and-myaql.git
cd login-system-with-flask-and-myaql
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Database Configuration
Before running the application, ensure you have configured your MySQL connection string in your settings.
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
CREATE DATABASE member_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE member_system;
CREATE TABLE `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(50) NOT NULL UNIQUE,    
    `password` VARCHAR(255) NOT NULL,          
    `email` VARCHAR(100) NOT NULL UNIQUE,   
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
### 5. Environment Variables Configuration (.env)
The application relies on environment variables to keep sensitive configuration secure. Create a file named `.env` in the root directory of the project and add the following variables:
```bash
DATABASE_URL=mysql+pymysql://username:password@host:port/database_name
SECRET_KEY=your_super_secret_random_key_here
```
### 6. Running the Application
```bash
python app.py
```
