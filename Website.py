from flask import Flask, request, redirect, url_for, flash, render_template_string
import re

app = Flask(__name__)

# Secret key for flash messages
app.secret_key = "my-secret-key-change-this"

# PORTFOLIO DATA

skills = [
    "Python",
    "Flask",
    "HTML",
    "CSS",
    "SQL",
    "Git",
    "IoT",
    "Java",
    "C",
    "Machine Learning"
]

projects = [
    {
        "title": "IoT Smart Home",
        "description": "A smart home system for monitoring and controlling devices.",
        "technologies": "Python, Arduino, MQTT",
        "github": "https://github.com/"
    },
    {
        "title": "Machine Learning Project",
        "description": "A machine learning application for data prediction.",
        "technologies": "Python, Pandas, Numpy, Scikit-learn",
        "github": "https://github.com/"
    },
    {
        "title": "Flask Portfolio",
        "description": "A responsive portfolio website created using Flask.",
        "technologies": "Python, Flask, HTML, CSS",
        "github": "https://github.com/"
    }
]

# COMPLETE HTML + CSS + JAVASCRIPT

HTML = """
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>My Portfolio</title>


    <style>

        /* 
           GENERAL
            */

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f5f7fb;
            color: #222;
            line-height: 1.6;
        }

        .container {
            width: 90%;
            max-width: 1100px;
            margin: auto;
        }


        /* 
           NAVBAR
            */

        .navbar {
            background: #111827;
            padding: 18px 0;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            color: white;
            text-decoration: none;
            font-size: 25px;
            font-weight: bold;
        }

        .nav-links {
            display: flex;
            gap: 25px;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }

        .nav-links a:hover {
            color: #6366f1;
        }


        /* ====================================================
           HERO
           ==================================================== */

        .hero {
            min-height: 85vh;
            display: flex;
            align-items: center;
        }

        .hero-content {
            max-width: 750px;
        }

        .hello {
            color: #4f46e5;
            font-size: 22px;
            font-weight: bold;
        }

        .hero h1 {
            font-size: 60px;
            margin: 10px 0;
        }

        .hero h2 {
            color: #555;
            font-size: 30px;
        }

        .hero p {
            margin-top: 20px;
            font-size: 18px;
        }


        /* ====================================================
           BUTTONS
           ==================================================== */

        .buttons {
            margin-top: 30px;
            display: flex;
            gap: 15px;
        }

        .btn {
            padding: 13px 25px;
            border-radius: 7px;
            text-decoration: none;
            display: inline-block;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }

        .primary {
            background: #4f46e5;
            color: white;
        }

        .secondary {
            background: #e5e7eb;
            color: #111;
        }

        .btn:hover {
            opacity: 0.85;
        }


        /* ====================================================
           SECTIONS
           ==================================================== */

        .section {
            padding: 80px 0;
        }

        .section-title {
            text-align: center;
            font-size: 38px;
            margin-bottom: 45px;
        }


        /* ====================================================
           SKILLS
           ==================================================== */

        .skills {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
        }

        .skill {
            background: white;
            padding: 12px 20px;
            border-radius: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            font-weight: bold;
        }


        /* ====================================================
           PROJECTS
           ==================================================== */

        .project-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
        }

        .project-card {
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            transition: 0.3s;
        }

        .project-card:hover {
            transform: translateY(-7px);
        }

        .project-card h3 {
            font-size: 23px;
            margin-bottom: 15px;
        }

        .technology {
            margin: 20px 0;
            color: #4f46e5;
            font-weight: bold;
        }

        .project-card a {
            color: #4f46e5;
            text-decoration: none;
            font-weight: bold;
        }


        /* ====================================================
           CONTACT
           ==================================================== */

        .contact-box {
            max-width: 700px;
            margin: auto;
        }

        .contact-form {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-top: 30px;
        }

        .contact-form label {
            font-weight: bold;
        }

        .contact-form input,
        .contact-form textarea {
            padding: 13px;
            border: 1px solid #ccc;
            border-radius: 7px;
            font-size: 16px;
            margin-bottom: 12px;
        }

        .contact-form textarea {
            resize: vertical;
        }


        /* ====================================================
           FLASH MESSAGES
           ==================================================== */

        .message {
            width: 90%;
            max-width: 1100px;
            margin: 20px auto;
            padding: 15px;
            border-radius: 7px;
            font-weight: bold;
        }

        .success {
            background: #dcfce7;
            color: #166534;
        }

        .error {
            background: #fee2e2;
            color: #991b1b;
        }


        /* ====================================================
           FOOTER
           ==================================================== */

        footer {
            background: #111827;
            color: white;
            text-align: center;
            padding: 30px;
            margin-top: 50px;
        }


        /* ====================================================
           MOBILE RESPONSIVE
           ==================================================== */

        @media (max-width: 768px) {

            .nav-container {
                flex-direction: column;
                gap: 15px;
            }

            .nav-links {
                gap: 15px;
            }

            .hero h1 {
                font-size: 42px;
            }

            .hero h2 {
                font-size: 23px;
            }

            .project-grid {
                grid-template-columns: 1fr;
            }

            .buttons {
                flex-direction: column;
            }

        }

    </style>

</head>


<body>


<!-- ========================================================
     NAVIGATION
     ======================================================== -->

<header class="navbar">

    <div class="container nav-container">

        <a href="/" class="logo">
            MyPortfolio
        </a>

        <nav class="nav-links">

            <a href="/">Home</a>

            <a href="/#skills">
                Skills
            </a>

            <a href="/#projects">
                Projects
            </a>

            <a href="/contact">
                Contact
            </a>

        </nav>

    </div>

</header>


<!-- ========================================================
     FLASH MESSAGES
     ======================================================== -->

{% with messages = get_flashed_messages(with_categories=true) %}

    {% if messages %}

        {% for category, message in messages %}

            <div class="message {{ category }}">

                {{ message }}

            </div>

        {% endfor %}

    {% endif %}

{% endwith %}


<!-- ========================================================
     HERO SECTION
     ======================================================== -->

<section class="hero">

    <div class="container hero-content">

        <div>

            <div class="hello">
                Hello, I'm
            </div>

            <h1>
                Abhay Vishwakarma
            </h1>

            <h2>
                Python & Flask Developer
            </h2>

            <p>
                I build web applications using Python,
                Flask, HTML, CSS and JavaScript.
                I am interested in IoT, embedded systems,
                machine learning and software development.
            </p>


            <div class="buttons">

                <a href="#projects"
                   class="btn primary">

                    View Projects

                </a>

                <a href="/contact"
                   class="btn secondary">

                    Contact Me

                </a>

            </div>

        </div>

    </div>

</section>


<!-- ========================================================
     SKILLS SECTION
     ======================================================== -->

<section class="section" id="skills">

    <div class="container">

        <h2 class="section-title">
            My Skills
        </h2>

        <div class="skills">

            {% for skill in skills %}

                <div class="skill">
                    {{ skill }}
                </div>

            {% endfor %}

        </div>

    </div>

</section>


<!-- ========================================================
     PROJECTS SECTION
     ======================================================== -->

<section class="section" id="projects">

    <div class="container">

        <h2 class="section-title">
            My Projects
        </h2>


        <div class="project-grid">

            {% for project in projects %}

                <div class="project-card">

                    <h3>
                        {{ project.title }}
                    </h3>

                    <p>
                        {{ project.description }}
                    </p>

                    <div class="technology">

                        {{ project.technologies }}

                    </div>

                    <a href="{{ project.github }}"
                       target="_blank"
                       rel="noopener noreferrer">

                        View on GitHub →

                    </a>

                </div>

            {% endfor %}

        </div>

    </div>

</section>


<!-- ========================================================
     FOOTER
     ======================================================== -->

<footer>

    <p>
        © 2026 My Portfolio
    </p>

    <p>
        Built with Python & Flask
    </p>

</footer>


<!-- ========================================================
     JAVASCRIPT
     ======================================================== -->

<script>

    // Automatically hide flash messages

    setTimeout(function () {

        const messages =
            document.querySelectorAll(".message");

        messages.forEach(function(message) {

            message.style.opacity = "0";

            message.style.transition = "opacity 0.5s";

            setTimeout(function() {

                message.remove();

            }, 500);

        });

    }, 4000);


    // Console message

    console.log(
        "Portfolio website loaded successfully!"
    );

</script>


</body>

</html>
"""


# HOME ROUTE

@app.route("/")
def home():

    return render_template_string(
        HTML,
        skills=skills,
        projects=projects
    )


# CONTACT ROUTE

@app.route("/contact", methods=["GET", "POST"])
def contact():

    # If user submits the form
    if request.method == "POST":

        name = request.form.get("name", "").strip()

        email = request.form.get("email", "").strip()

        message = request.form.get("message", "").strip()


        # Validation
        
        if not name or not email or not message:

            flash(
                "All fields are required.",
                "error"
            )

            return redirect(url_for("contact"))


        # Email validation

        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(email_pattern, email):

            flash(
                "Please enter a valid email address.",
                "error"
            )

            return redirect(url_for("contact"))


        # Message length validation

        if len(message) < 10:

            flash(
                "Message must contain at least 10 characters.",
                "error"
            )

            return redirect(url_for("contact"))

        # Display submitted data in terminal

        print("NEW CONTACT MESSAGE")

        print("Name:", name)

        print("Email:", email)

        print("Message:", message)



        # Success message

        flash(
            "Your message has been sent successfully!",
            "success"
        )

        return redirect(url_for("contact"))

    # Contact page
    
    contact_html = """

    <!DOCTYPE html>

    <html>

    <head>

        <title>Contact | My Portfolio</title>

        <style>

            body {
                font-family: Arial;
                background: #f5f7fb;
                margin: 0;
                padding: 0;
            }

            .container {
                width: 90%;
                max-width: 700px;
                margin: auto;
            }

            nav {
                background: #111827;
                padding: 20px;
            }

            nav a {
                color: white;
                text-decoration: none;
                margin-right: 20px;
                font-weight: bold;
            }

            .contact {
                margin-top: 70px;
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            }

            h1 {
                font-size: 40px;
            }

            form {
                display: flex;
                flex-direction: column;
                gap: 10px;
            }

            input,
            textarea {
                padding: 13px;
                border: 1px solid #ccc;
                border-radius: 6px;
                font-size: 16px;
            }

            textarea {
                resize: vertical;
            }

            button {
                background: #4f46e5;
                color: white;
                padding: 14px;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 16px;
            }

            button:hover {
                opacity: 0.85;
            }

        </style>

    </head>


    <body>

        <nav>

            <a href="/">
                Home
            </a>

            <a href="/contact">
                Contact
            </a>

        </nav>


        {% with messages = get_flashed_messages(with_categories=true) %}

            {% if messages %}

                {% for category, message in messages %}

                    <p style="
                        padding:15px;
                        text-align:center;
                        background:#dcfce7;
                        color:#166534;
                    ">

                        {{ message }}

                    </p>

                {% endfor %}

            {% endif %}

        {% endwith %}


        <div class="container">

            <div class="contact">

                <h1>
                    Contact Me
                </h1>

                <p>
                    Have a project or job opportunity?
                    Send me a message.
                </p>


                <form method="POST"
                      action="/contact">


                    <label>
                        Name
                    </label>

                    <input
                        type="text"
                        name="name"
                        placeholder="Enter your name"
                        required
                    >


                    <label>
                        Email
                    </label>

                    <input
                        type="email"
                        name="email"
                        placeholder="Enter your email"
                        required
                    >


                    <label>
                        Message
                    </label>

                    <textarea
                        name="message"
                        rows="7"
                        placeholder="Write your message..."
                        required
                    ></textarea>


                    <button type="submit">

                        Send Message

                    </button>

                </form>

            </div>

        </div>

    </body>

    </html>

    """

    return render_template_string(contact_html)


# 404 ERROR HANDLER

@app.errorhandler(404)
def page_not_found(error):

    return """
    <div style="
        text-align:center;
        margin-top:100px;
        font-family:Arial;
    ">

        <h1 style="font-size:70px;">
            404
        </h1>

        <h2>
            Page Not Found
        </h2>

        <p>
            The page you are looking for does not exist.
        </p>

        <a href="/">
            Go Back Home
        </a>

    </div>
    """, 404

# START FLASK APPLICATION

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
