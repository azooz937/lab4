# apps/bookmodule/urls.py

from django.urls import path
from . import views
from apps.bookmodule import views as bookmoduleviews


urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('index2/<int:val1>/', bookmoduleviews.index2, name='index2'),
]
