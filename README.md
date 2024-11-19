# Student Management System

This project is a simple Django-based Student Management System that allows administrators to manage students and user authentication for registration, login, and logout.

## Features

- **User Authentication**:
  - User registration.
  - Login and logout functionality.
  - Authentication checks for user permissions.

- **Student Management**:
  - Create, view, update, and delete student records.
  - Search for a student by their ID.
  - Admin-only access for creating, updating, and deleting students.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Django 4.x or higher
- A virtual environment tool (optional but recommended)

## Usage

### Authentication
- **Register**: Access the registration page at `/register/` to create a new account.
- **Login**: Login at `/login/` using your credentials.
- **Logout**: Logout at `/logout/`.

### Student Management
- **View All Students**: Navigate to `/students/` to see the list of all students.
- **Create a Student**: Access `/students/create/` (admin-only).
- **Search for a Student**: Use the search functionality on the student view page `/students/view/`.
- **Update a Student**: Navigate to `/students/update/<student_id>/` (admin-only).
- **Delete a Student**: Access `/students/delete/<student_id>/` (admin-only).
