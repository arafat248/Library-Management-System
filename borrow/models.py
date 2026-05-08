from django.db import models
from accounts.models import User
from books.models import Book

# Create your models here.
class Borrow(models.Model):
    STATUS_CHOICES=(
        ('borrowed', 'Borrrowed'),
        ('returned', 'Returned')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    due_date = models.DateField()
    fine = models.DecimalField( max_digits=5, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='borrowed')
    
    def __str__(self):
        return f"{self.user.user_name}-{self.book.title}"