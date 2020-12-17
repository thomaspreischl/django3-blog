from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    inhalt = models.CharField(max_length=250, default='Text')
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
