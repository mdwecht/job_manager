from django.db import models


class App(models.Model):
    name = models.CharField(max_length=50, default='<app name>')
    job_module = models.CharField(max_length=40, default='<model module>')
    job_name = models.CharField(max_length=40, default='<model name>')
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name    
