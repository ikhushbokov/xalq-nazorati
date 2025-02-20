from django.db import models
from users.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver


class CaseTypes(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Case(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cases", null=True, blank=True)
    case_type = models.ForeignKey(CaseTypes, on_delete=models.CASCADE)
    description = models.TextField()
    manual_address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    case_number = models.PositiveIntegerField(unique=True, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Case #{self.case_number} - {self.user.full_name}"

    def clean(self):
        if not self.description:
            raise ValidationError("Description is required.")
        if not self.manual_address and (self.latitude is None or self.longitude is None):
            raise ValidationError("Either manual address or latitude and longitude should be provided.")

    @property
    def get_address(self):
        if self.manual_address:
            return self.manual_address
        return f"Lat: {self.latitude}, Long: {self.longitude}"

    class Meta:
        ordering = ['-created_time']


@receiver(pre_save, sender=Case)
def set_case_number(sender, instance, **kwargs):
    if not instance.case_number:
        last_case = Case.objects.order_by('-case_number').first()
        instance.case_number = (last_case.case_number + 1) if last_case else 1


class CaseImage(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="images")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="case_images", null=True, blank=True)
    video = models.FileField(upload_to='cases/videos/', blank=True, null=True)
    image = models.ImageField(upload_to='cases/images/', blank=True, null=True)

    def clean(self):
        if not self.image and not self.video:
            raise ValidationError('You must upload either an image or a video.')
        if self.image and self.video:
            raise ValidationError('You can only upload either an image or a video, not both.')

    def __str__(self):
        return f"Image for Case {self.case.case_number} by {self.user.full_name}"
