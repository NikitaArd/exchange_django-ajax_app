from django.urls import path
from .views import index
from .views import post_index

urlpatterns = [
    path('', index, name='index'),
    path('post/ajax/exchange', post_index, name='post_index'),
]
