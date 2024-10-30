## Library Management System
A Library Management System built using Python's Tkinter for the GUI and MySQL for database management, accessed via XAMPP. This application enables users to sign up, sign in, and borrow books. It includes admin functionalities to manage user data, book inventory, and borrowing records.

## Features
- User Authentication: Supports user sign-up, login, and an admin login with specific credentials.
- Admin Capabilities: Allows admin to view all users, books, and borrowed book records.
- Borrowing Books: Users can borrow books and view available book lists.
- GUI: Designed with a Tkinter interface, including TTK styles for enhanced UI components.
- 
## Tech Stack
- Frontend: Tkinter (Python GUI library)
- Backend: MySQL (using XAMPP for database management)
- Database Management: MySQL Connector

## Table of Contents
- [Installation]
- [Database Setup]
- [Usage]
- [Directory Structure]
- [Screenshots]
- [Troubleshooting]

## Installation
1. Clone the Repository
   ```bash
   git clone
   cd library-management-system
2. Install Requirements
   ```bash
   pip install mysql-connector-python
3. Start XAMPP
   Launch XAMPP and start the Apache and MySQL modules

## Database Setup
1. Open phpMyAdmin in your browser.
2. Create a database named library.
3. Import library.sql (included in the project directory) to set up the necessary tables.

## Usage
1. Run the Application
   ```bash
   python app.py
2. Sign Up/ Sign In
   - New users can sign up by providing details
   - Users can log in afterwards
3. Admin Login
   - Admin can log in using:
       - Username: admin
       - Password: admin123
## Directory Structure
      ```bash
     ├── app.py                  # Main application file
     ├── admin.py                # Admin functionality
     ├── sign_up.py              # User sign-up functionality
     ├── user_borrow.py          # Book borrowing functionality
     ├── library.sql             # SQL file to set up the database
     ├── README.md               # Project documentation
     └── requirements.txt        # Required Python packages
## Troubleshooting
- Database Connection Issues: Ensure XAMPP is running and the database library is created in phpMyAdmin.
