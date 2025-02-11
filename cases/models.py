from django.db import models
from users.models import User
from django.core.exceptions import ValidationError


class CaseTypes(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Case(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cases",  null=True, blank=True)
    case_type = models.ForeignKey(CaseTypes, on_delete=models.CASCADE)
    description = models.TextField()
    manual_address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    case_number = models.PositiveIntegerField(default=1)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def clean(self):
        if not self.description:
            raise ValidationError("Description is required.")
        if not self.manual_address and (self.latitude is None or self.longitude is None):
            raise ValidationError("Either manual address or latitude and longitude should be provided.")

    def __str__(self):
        if self.manual_address:
            return self.manual_address
        return f"Lat: {self.latitude}, Long: {self.longitude}"

    class Meta:
        ordering = ['-created_time']


class CaseImage(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    video = models.FileField(upload_to='cases/', blank=True, null=True)
    image = models.ImageField(upload_to='cases/', blank=True, null=True)

    def __str__(self):
        return str(self.case)