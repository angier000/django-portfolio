from django.urls import path
from . import views

urlpatterns = [
    # defines url patter
    # '' matches root url of app, then maps to index function from views
    # 'index' is name accosiated with this url
    path('', views.index, name='index'),
]