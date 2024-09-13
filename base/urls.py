from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate,DeleteView, CustomLoginView, RegisterPage, TaskReorder
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.contrib import admin
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', views.home,name='home'),
    path("drugs",views.drugs,name='drugs'),
   path("<int:id>/",views.detail,name='detail'),
   
   path("aboutus",views.aboutus,name='aboutus'),
   path("resources",views.resources,name='resources'),
   path("education",views.education,name='education'),
 
   path("tue",views.tue,name='tue'),
   
    path('tasks', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
    
       
     path("stage",views.stage,name='stage'),
    path("tue_form",views.tue_form,name='tue_form'),
    path("upload",views.upload,name='upload'),
    path("info",views.info,name='info'),
    path("news",views.news,name='news'),
   path("prescription",views.prescription,name='prescription'),
   
   path("doctorLog",views.doctorLog,name='doctorLog'),
   path("pre",views.pre,name='pre'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
