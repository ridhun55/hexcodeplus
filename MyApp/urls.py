
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.homeView,name='home'),
    path('myadmin/', views.adminView,name='myadmin'),
    path('enquiry_home/', views.enquiry_homeView,name='enquiry_home'),
    path('enquiry_delete/<int:id>', views.enquiry_deleteView,name='enquiry_delete'),
    path('employee_upload/', views.employeeuploadView,name='employee_upload'),
    path('employee_delete/<int:id>', views.employee_deleteView,name='employee_delete'),
    path('employee<int:id>', views.employeeView,name='employee'),

    path('blog_upload_technology/', views.blog_upload_technologyView,name='blog_upload_technology'),
    path('blog_technology_delete/<int:id>', views.blog_technology_deleteView,name='blog_technology_delete'),
    path('blog_home_technology/', views.blog_home_technologyView,name='blog_home_technology'),
    path('blog_technology/<int:id>', views.blog_technologyView,name='blog_technology'),

    path('blog_upload_tutorials/', views.blog_upload_tutorialsView, name='blog_upload_tutorials'),
    path('blog_tutorials_delete/<int:id>', views.blog_tutorials_deleteView, name='blog_tutorials_delete'),
    path('blog_home_tutorials/', views.blog_home_tutorialsView, name='blog_home_tutorials'),
    path('blog_tutorials/<int:id>', views.blog_tutorialsView, name='blog_tutorials'),

    path('blog_upload_circuits/', views.blog_upload_circuitsView, name='blog_upload_circuits'),
    path('blog_circuits_delete/<int:id>', views.blog_circuits_deleteView, name='blog_circuits_delete'),
    path('blog_home_circuits/', views.blog_home_circuitsView, name='blog_home_circuits'),
    path('blog_circuits/<int:id>', views.blog_circuitsView, name='blog_circuits'),
]
