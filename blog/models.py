from django.db import models

# Create your models here.

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}, created {self.created}'
    
    class Meta:
        ordering = ['-created']
