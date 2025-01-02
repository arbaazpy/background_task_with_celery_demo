from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.id} --- {self.first_name} {self.last_name}"
