import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logistics.settings')
django.setup()

from payment.models import payment

payment.objects.all().delete()