from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=300)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}  {self.category.name}'


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

