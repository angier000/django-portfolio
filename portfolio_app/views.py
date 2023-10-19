from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import ProjectForm #, PortfolioForm
from django.contrib import messages

# Create your views here.
def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    
    # Render the HTML template index.html with the data in the context variable.
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

class PortfolioDetailView(generic.DetailView):
    model = Portfolio

    # override get_context_data method, change context data that will be passed to template
    def get_context_data(self, **kwargs):

        # call method parent class (PortfolioDetailView) and get data from original method
        context = super().get_context_data(**kwargs)

        # get current portfolio
        current = self.get_object()

        # get projects associated with current portfolio
        projects = Project.objects.filter(portfolio=current)

        # add context info
        context['projects'] = projects

        # return updated context
        return context

class ProjectListView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project

def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy() # copy of post data
        project_data['portfolio_id'] = portfolio_id # associate new project with correct portfolio
        
        # create new instance of ProjectForm with updated data
        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            # save to database
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)


def deleteProject(request, portfolio_id, project_id):
    # get the portfolio
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)

    # get the project
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        # check if project belongs to the correct portfolio
        if project.portfolio == portfolio:
            project.delete()
            return redirect('portfolio-detail', portfolio_id)
        
        # pass project to template to confirm deletion
        context = {'portfolio': portfolio, 'project': project}
        return render(request, 'portfolio_app/project_delete.html', context)
    
    # handle GET requests (shows confirmation page)
    context = {'portfolio': portfolio, 'project': project}
    return render(request, 'portfolio_app/project_delete.html', context)