from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    category = models.CharField(category, on_delete=models.CASCADE, releted_name='books')
    isbn = models.CharField()
    descriptions = models.TextField()
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    #image = models.ImageField(upload_to=book/images)
    published_date = models.DateField()
    created_at = models.DateField(auto_now_add=False)

    def __set__(self):
        return f"{self.title} {self.descriptions}"
