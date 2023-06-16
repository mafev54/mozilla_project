from django.db import models
from django.urls import reverse
from .book import Book

class BookInstance(models.Model):
    unique_id = models.CharField(max_length=50)
    due_back = models.DateField(default=0)
    LOAN_STATUS = (
        ('Maintenance', 'Maintenance'),
        ('On loan', 'On loan'),
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
    )

    status = models.CharField(
        max_length=15,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    book = models.OneToOneField(Book, null = True, on_delete=models.SET_NULL)
    imprint = models.CharField(max_length=50)
    borrower = models.CharField(max_length=50)

    def str(self):
        return self.unique_id

    def get_absolute_url(self):
        return reverse('book_instance-detail', args=[str(self.id)])