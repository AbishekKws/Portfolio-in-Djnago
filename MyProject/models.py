from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    mage = models.ImageField(upload_to='Project/images', null=True, blank=True)
    link = models.URLField()

    def __str__(self):
        return self.title
    