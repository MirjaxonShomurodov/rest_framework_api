from .views import Index,AddTask
from django.urls import path
urlpatterns = [
    path("index/",Index.as_view(),name='index'),
    path('add/',AddTask.as_view(),name='add')
]