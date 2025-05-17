from django.db import models
from django.utils import timezone
import uuid

class EmailOTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4)  # Placeholder for securing user

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=1)
