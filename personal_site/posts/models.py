from django.db import models

# Create your models here.
class Job(models.Model):
    company_name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='images/')
    job_title = models.CharField(max_length=150)
    date_range = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.job_title

class Skill(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.TextField()
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    github_link = models.TextField(null=True, blank=True)
    hosted_link = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title