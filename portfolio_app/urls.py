from django.urls import path
from . import views

urlpatterns = [
    # defines url pattern
    # '' matches root url of app, then maps to index function from views
    # 'index' is name associated with this url
    path('', views.index, name='index'),
    path('students/', views.StudentListView.as_view(), name= 'students'), 
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('projects/', views.ProjectListView.as_view(), name= 'projects'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('portfolio/<int:portfolio_id>/create_project/', views.createProject, name='create_project'),
] 