from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
# from .forms import ProjectForm, PortfolioForm
from django.contrib import messages

# Create your views here.
def index(request):
    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'portfolio_app/index.html')

class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

class PortfolioDetailView(generic.DetailView):
    model = Portfolio