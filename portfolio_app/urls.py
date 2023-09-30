from django.urls import path
from . import views

urlpatterns = [
    # defines url pattern
    # '' matches root url of app, then maps to index function from views
    # 'index' is name associated with this url
    path('', views.index, name='index'),
]