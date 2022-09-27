from django.shortcuts import render
from rest_framework import viewsets
from ManageBook.models import BookmanageModel
from ManageBook.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookmanageModel.objects.all()
    serializer_class = BookSerializer
