from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, unique=True)
    passport = models.CharField(max_length=9, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.full_name