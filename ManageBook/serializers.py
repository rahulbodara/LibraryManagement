from pyexpat import model
from rest_framework import serializers
from ManageBook.models import BookmanageModel

class BookSerializer(serializers.ModelSerializer):
    class Meta():
        model = BookmanageModel
        fields = ('id','book_type','account_number','book_title','book_author','book_publisher','bill_number','book_price','ISBN_number','remarks','softcopy')