from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Formulary(models.Model):
    user_name = models.CharField(max_length=20)
    user_surname = models.CharField(max_length=20)
    user_email = models.CharField(max_length=40)
    change = models.CharField(max_length=30)
    change_description = models.CharField(max_length=120)
    change_justification = models.CharField(max_length=120)
    PRIORITY_CHOICES = [
        ("Low", "Baja"),
        ("Medium", "Media"),
        ("High", "Alta"),
    ]
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default="Low")
    STATUS_CHOICES = [
        ("Pending", "Pendiente"),
        ("Approved", "Aprobado"),
        ("Rejected", "Rechazado"),
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="Pending")
    comment = models.CharField(max_length=120, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.change
