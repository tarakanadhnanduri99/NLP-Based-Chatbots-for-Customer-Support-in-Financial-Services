import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinBotFrontEnd.settings')

# Import Django and set it up
import django
django.setup()

from FinBot import trainer

if __name__ == "__main__":
    trainer.train_intent_model() 