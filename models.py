from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=40)
    sec_to_next = models.IntegerField(default=3600)
    params_tb = models.CharField(max_length=40)
    params_id = models.IntegerField(default=0)
    ran_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name    
