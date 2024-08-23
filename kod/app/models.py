from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class BotUsers(models.Model):
    user_id=models.CharField(max_length=120)
    first_name=models.TextField(max_length=250)
    last_name=models.TextField(max_length=250)
    age=models.IntegerField()
    email=models.EmailField()
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?\d{10,15}$', 'Enter a valid phone number')],
        blank=True,  # Allow blank if not always required
        null=True    # Allow null if not always required
    )

    def __str__(self) -> str:
        return f"{self.first_name}"
    