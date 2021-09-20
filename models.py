from django.db import models

# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=50)
    job_table = models.CharField(max_length=40)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name    
