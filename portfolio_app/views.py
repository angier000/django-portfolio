from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.views import generic

# Create your views here.
def index(request):
    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'portfolio_app/index.html')

class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student
