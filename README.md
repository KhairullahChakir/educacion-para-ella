# Maktab - Online Learning Platform for Afghan Students

## Quick Start

1. **Activate virtual environment:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```powershell
   Copy-Item .env.example .env
   # Edit .env with your PostgreSQL credentials
   ```

4. **Create the database:**
   ```sql
   psql -U postgres
   CREATE DATABASE maktab;
   \q
   ```

5. **Run migrations:**
   ```powershell
   python manage.py migrate
   ```

6. **Install Tailwind CSS:**
   ```powershell
   python manage.py tailwind install
   ```

7. **Start development server (two terminals):**
   ```powershell
   # Terminal 1 - Tailwind watcher
   python manage.py tailwind start

   # Terminal 2 - Django server
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/`

## Tech Stack

- **Backend:** Python + Django 5.2
- **Frontend:** HTML + Tailwind CSS + JavaScript
- **Database:** PostgreSQL
- **Authentication:** Django built-in auth
