from django.db import models
from model_utils import Choices

# Create your models here.
class BookmanageModel(models.Model):
    BOOK_TYPES = Choices(
        ("book","Book"),
        ("magazine","Magazine"),
    )
    book_type = models.CharField(max_length=10,choices=BOOK_TYPES)
    account_number = models.PositiveBigIntegerField()
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_publisher = models.CharField(max_length=100)
    bill_number = models.PositiveBigIntegerField()
    book_price = models.DecimalField(max_digits=10, decimal_places=2)
    ISBN_number = models.PositiveBigIntegerField()
    remarks = models.TextField()
    softcopy = models.FileField(upload_to='uploads/')

    class Meta:
        db_table = 'books_tbl'

    def __str__(self):
        return f'{self.book_title}'
 