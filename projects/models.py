from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    in_progress = models.BooleanField()
    blogpost = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-end_date']

class Image(models.Model):
    # image = models.ImageField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
