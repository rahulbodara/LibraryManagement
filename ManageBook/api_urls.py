from django.urls import include, path
from rest_framework import routers
from ManageBook import views
router = routers.DefaultRouter()
router.register(r'book-operations', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]