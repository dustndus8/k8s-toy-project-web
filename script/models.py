from django.db import models

# Create your models here.
FLAVOR_CHOICES = (
    ('x1.small','X1.SMALL'),
    ('x1.medium','X1.MEDIUM'),
    ('x1.large','X1.LARGE'),
)

class Script(models.Model):
    project_name = models.CharField(max_length=40)
    key_pair_name = models.CharField(max_length=40)
    flavor = models.CharField(choices=FLAVOR_CHOICES, default='x1.small')
    worker = models.IntegerField()