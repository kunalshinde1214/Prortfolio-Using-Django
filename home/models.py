from django.db import models

class home(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  enroll_id = models.IntegerField(default=0)

# Create your models here.
def __str__(self):
    return f"{self.firstname} {self.lastname}"