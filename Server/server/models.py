from django.db import models

class CustomUser(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)

    # https://docs.djangoproject.com/en/5.1/ref/models/instances/#django.db.models.Model.__str__
    def __str__(self):
        return CustomUser(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name
        )