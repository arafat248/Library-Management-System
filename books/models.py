from django.db import models
from category.models import Category

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField()
    descriptions = models.TextField()
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    #image = models.ImageField(upload_to=book/images)
    published_date = models.DateField()
    created_at = models.DateField(auto_now=False)

    def __str__(self):
        return self.title
