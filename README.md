# Mini-Website

# Flask Portfolio Website
## Project Overview
This project is a personal portfolio website developed using Python and Flask. It provides a simple and responsive platform to showcase programming skills, projects, technologies, and contact information.
The website includes a home page with an introduction, skills section, project section, contact page, form validation, flash messages, responsive styling, and a custom 404 error page.
The application demonstrates how Flask can be used to create a functional web application with HTML, CSS, JavaScript, Python routing, form handling, and input validation.

## Features
* Responsive personal portfolio website
* Flask-based backend
* Home page with personal introduction
* Skills section
* Projects section
* Project technology information
* GitHub project links
* Contact page
* Contact form
* Name, email, and message validation
* Email format validation using regular expressions
* Minimum message length validation
* Flask flash messages for success and error notifications
* Custom 404 Page Not Found handler
* Responsive mobile design
* Sticky navigation bar
* Automatic hiding of flash messages
* JavaScript console message
* Clean and simple user interface

## Technologies Used
### Backend
* Python
* Flask
* Regular Expressions

### Frontend
* HTML5
* CSS3
* JavaScript

## Project Structure

```text
Flask-Portfolio/
│
├── Website.py
└── README.md
```

## Main Application

The main Python file is `Website.py`. It contains the Flask application, portfolio data, HTML, CSS, JavaScript, routes, contact form processing, validation, and error handling.

The Flask application is initialized using:

```python
from flask import Flask, request, redirect, url_for, flash, render_template_string
import re

app = Flask(__name__)
```

A secret key is configured for Flask flash messages.

## Portfolio Sections

### Home Section
The home page introduces the portfolio owner as a Python and Flask developer. It also provides information about interests in IoT, embedded systems, machine learning, and software development.
The page provides buttons for viewing projects and accessing the contact page.

### Skills Section
The website displays a collection of technical skills including:
* Python
* Flask
* HTML
* CSS
* SQL
* Git
* IoT
* Java
* C
* Machine Learning
These skills are stored in a Python list and dynamically displayed using a Jinja template loop.

### Projects Section
The portfolio contains project cards with a project title, description, technologies used, and GitHub link.
The included projects are:
1. IoT Smart Home
2. Machine Learning Project
3. Flask Portfolio
The project information is stored in Python dictionaries and dynamically displayed on the website.

## Contact Form
The website includes a dedicated `/contact` route that supports both GET and POST requests.
Users can enter:
* Name
* Email
* Message
The form submits the information to the Flask backend for processing.

## Form Validation
The application performs several validation checks before accepting a contact message.

### Required Fields
The application checks whether the name, email, and message fields contain values.
If any field is empty, an error message is displayed.

### Email Validation

A regular expression is used to check whether the submitted email follows a valid email format.

```python
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
```

If the email format is invalid, the user receives an error message.

### Message Length Validation
The application requires the message to contain at least 10 characters.
If the message is shorter than 10 characters, an error message is displayed.

## Flash Messages
Flask flash messages are used to provide feedback after form submission.
The application displays success and error messages depending on the result of validation.
JavaScript automatically hides these messages after a few seconds, providing a cleaner user experience.

## Responsive Design
The website is designed to work on both desktop and mobile screens.
A CSS media query is used for screens with a maximum width of 768 pixels. On smaller screens:
* Navigation elements become vertically arranged
* Heading sizes are reduced
* Project cards change to a single-column layout
* Buttons are arranged vertically
This makes the website more suitable for mobile devices.

## Navigation
The website contains a sticky navigation bar with links to:
* Home
* Skills
* Projects
* Contact
The navigation remains visible while scrolling through the page.

## 404 Error Handling
A custom 404 error handler is included in the Flask application.
If a user visits a page that does not exist, the application displays a custom "404 Page Not Found" message with an option to return to the home page.

## How to Run the Project
### Step 1: Install Python
Make sure Python is installed on your computer.
Check the installation using:

```bash
python --version
```

or:

```bash
py --version
```

### Step 2: Open the Project in VS Code
Open the project folder in Visual Studio Code.
Make sure `Website.py` is inside the project folder.
### Step 3: Install Flask
Open the VS Code terminal and run:

```bash
pip install flask
```

If `pip` does not work, try:

```bash
python -m pip install flask
```

### Step 4: Run the Application

Run:

```bash
python Website.py
```

The application starts the Flask development server on:

```text
http://127.0.0.1:5000
```

The application is configured to run on port 5000 with Flask debug mode enabled.

### Step 5: Open the Website

Open a web browser and visit:

```text
http://127.0.0.1:5000
```

The portfolio home page should now be displayed.

## Contact Page
To open the contact page directly, visit:

```text
http://127.0.0.1:5000/contact
```

The contact form allows users to enter their name, email address, and message.
After successful validation, the submitted information is printed in the terminal and a success message is displayed.

## Important Note
The current contact form does not send an actual email. The submitted name, email, and message are printed in the terminal by the Flask application.
For a production website, an email service or database could be integrated to store or deliver contact messages.

## Security Note
The project currently contains a Flask secret key directly inside the Python source code:

```python
app.secret_key = "my-secret-key-change-this"
```

For a real production application, this value should be replaced with a secure secret key and stored using an environment variable rather than committing it directly to GitHub.

## Future Improvements
The project can be further improved by adding:
* A separate `templates` folder
* A separate `static` folder for CSS and HTML
* Database integration
* Real email functionality
* Admin dashboard
* Resume download option
* Social media links
* Project images
* Project filtering
* Dark mode
* Deployment to a cloud hosting platform
* Environment variables for sensitive configuration
* Improved form security
* CSRF protection

## Learning Outcomes
Through this project, the following concepts are demonstrated:
* Creating a Flask application
* Creating Flask routes
* Handling GET and POST requests
* Processing HTML form data
* Validating user input
* Using regular expressions
* Using Flask flash messages
* Using Jinja template syntax
* Creating responsive web pages
* Combining Python with HTML, CSS
* Handling HTTP 404 errors
* Running a Flask development server
