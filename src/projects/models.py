from django.db import models

class Project(models.Model):
    title = models.TextField()
    summary = models.TextField()
    skills = models.TextField()
    pub_date = models.DateTimeField("date published")
    github = models.URLField()
    external = models.URLField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title