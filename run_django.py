import os
import sys
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinBotFrontEnd.settings')

# Set up Django
django.setup()

# Import the Django application
from FinBot import views

if __name__ == "__main__":
    # This is just a placeholder. In a real application, you would use Django's runserver
    # or a WSGI server like Gunicorn or uWSGI.
    print("Django application is set up correctly.")
    print("To run the application, use: python manage.py runserver") 