from django.db import models


class Developer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    alias = models.CharField(max_length=20,  null=True, blank=True)
    avatar = models.ImageField(upload_to="developer_pics/", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"







class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    github_url = models.URLField()
    gist_link = models.CharField()
    image = models.ImageField(upload_to="project_pics/")
    developer = models.ManyToManyField(Developer)



