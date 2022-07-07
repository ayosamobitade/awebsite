from django.db import models

# Create your models here.
from django.contrib.auth.models import User

STATUS_CHOICE = (
('NEW', 'New Site'),
('Ex', 'Existing Site'),
)

PRIORITY_CHOICES = (
    ('U', 'Urgent - 1 week or less'),
    ('N', 'Normal - 2 to 4 weeks'),
    ('L', 'Low - Still Researching'),
)

class Quote(models.Model):
    name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 60, blank = True)
    company = models.CharField(max_length = 60, blank = True)
    address =  models.CharField(max_length = 200, blank = True)
    phone = models.CharField(max_length = 200, blank = True)
    email = models.EmailField()
    web = models.URLField(blank = True)
    