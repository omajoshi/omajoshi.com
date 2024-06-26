from django.db import models

# Create your models here.

class ResearchProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    in_progress = models.BooleanField()
    blogpost = models.ForeignKey('blog.Post', on_delete=models.CASCADE, null=True, blank=True)
    # link = models.URLField(null=True, blank=True)
    # source = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_date', '-end_date']

class Image(models.Model):
    # image = models.ImageField()
    project = models.ForeignKey('ResearchProject', on_delete=models.CASCADE, null=True, blank=True)
