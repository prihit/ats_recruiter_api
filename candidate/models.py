from django.db import models

# Create your models here.
class Candidate(models.Model):
    STATUS_CHOICES = (
        ('Applied', 'Applied'),
        ('Rejected', 'Rejected'),
        ('Shortlisted', 'Shortlisted'),
    )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    years_of_exp = models.FloatField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    current_salary = models.FloatField()
    expected_salary = models.FloatField()
    status = models.CharField(max_length=20, default="Applied", choices=STATUS_CHOICES)