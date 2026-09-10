# Edu-Adapt

Edu-Adapt is a Flask and MySQL study companion that adapts a learner's plan to due dates, task priority, unit completion, and recent study activity.

## Included features

- Account registration and secure password hashing
- Subjects, units, task tracking, and a due-date calendar
- An adaptive task plan and workload-risk score
- Pomodoro/study-session recording and learning analytics
- GPA outcome simulation, personalised recommendations, reflections, and notifications

## Run locally with XAMPP

1. Start **MySQL** in XAMPP. The project is already configured for the existing `eduadapt` database.
2. In this project folder, create a virtual environment and install dependencies:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. Check `.env`. The defaults match a standard local XAMPP installation (`root` with no password).
4. Start the app:

   ```powershell
   python app.py
   ```

5. Visit `http://127.0.0.1:5000`, create an account, then add subjects and tasks.

`database/eduadapt.sql` is a portable schema export for a fresh installation. It does not need to be imported when using your existing database.

## Project layout

The folders follow the requested separation of routes, services, domain models, algorithms, templates, static assets, utilities, database scripts, and tests.
