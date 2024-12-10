from django.db import models
from django.urls import reverse

# Create your models here.
class studytable(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Amount = models.IntegerField(default=0, blank=True)
    Username=models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

class PageVisit(models.Model):
    count = models.IntegerField(default=0)


class Comment(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        ordering = ["-created_at"]


class studytable1(models.Model):
    Firstname=models.CharField(max_length=100)
    Age=models.IntegerField()
    Email=models.EmailField()
    Mob=models.IntegerField()

    def __str__(self):
        return self.Firstname

    def get_absolute_url(self):
        return reverse('studyapp8:studytable1-detail', args=[str(self.id)])