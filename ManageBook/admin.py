from django.contrib import admin
from ManageBook.models import BookmanageModel
# Register your models here.

@admin.register(BookmanageModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','book_type','account_number','book_title','book_author','book_publisher','bill_number','book_price','ISBN_number','remarks','softcopy')