# Specimen Classifier System

A system customly made for managing data relating to biological specimens.

This project is still in development stage. It wil temporarily use sqlite3 before fully migrating to postgresql.
All data that will be created will only remain as a test data.

### Setup Guidelines

1. Make sure that you have git and Python 3.7.6 installed in your machine.
2. If you still don't have virtualenv installed, run `pip install virtualenv`
3. Create and activate a virtual environment.
```bash
virtualenv venv
```

Windows:
```
venv\Scripts\activate
```

Mac/Linux
```
source venv/bin/activate
```

4. In your terminal, cd to your desired directory and clone this repository.
5. Run `pip install -r requirements.txt`
6. Run `python manage.py migrate`
7. To run the project, enter `python manage.py runserver.`
