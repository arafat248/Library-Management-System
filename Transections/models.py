from django.db import models
from django.utils import timezone
from accounts.models import User
from books.models import Book

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=False)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    fine_per_day = 20  # taka per day late
    fine_amount = models.IntegerField(default=0)
    def calculate_fine(self):
        if self.return_date and self.return_date > self.due_date:
            late_days = (self.return_date - self.due_date).days
            return late_days * self.fine_per_day
        return 0
    def save(self, *args, **kwargs):
        if self.return_date:
            self.fine_amount = self.calculate_fine()
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.user.username} - {self.book.title}"