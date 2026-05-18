# Login System With Flask And MySQL
A simple project for a membership system built with Flask and MySQL, featuring registration, and an administrative member list view.
</br>[View Live Project](http://54.65.199.159)
</br></br>
<img width="490" height="569" alt="image" src="https://github.com/user-attachments/assets/7e89037a-35c9-4c97-b516-9f03c717aabe" />

> **Testing Credentials**
> 
> You can create your own account using the sign-up feature, or use the pre-configured test accounts below:
> 
> | Role | Username | Password | Note |
> | :--- | :--- | :--- | :--- |
> | **Regular User** | `test` | `test` | Standard member access |
> | **Administrator** | `admin` | `admin` | Can view the administrative member list |

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
git clone https://github.com/gpna1229/login-system-with-flask-and-mysql.git
cd login-system-with-flask-and-mysql
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Database Configuration
Before running the application, ensure you have configured your MySQL connection string in your settings.
#### Database Schema

The application uses a MySQL database with a single `users` table to manage membership data. 
</br>If you don't have MySQL installed yet, you can download it from the [MySQL Official Downloads](https://dev.mysql.com/downloads/) page.

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
## Roadmap & TODOs
Here are the upcoming features and improvements planned for this project:
- [ ] **Robust Input Validation**: Implement strict rules for registration (e.g., strong password requirements, email format checks, and character length limits).
- [ ] **Enhanced Error Handling**: Improve user experience by handling authentication failures gracefully (e.g., displaying specific error messages for "Incorrect password" or "Username does not exist").
