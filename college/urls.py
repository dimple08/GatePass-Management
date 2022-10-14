from . import views
from django.urls import path

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('loginadmin/', views.adminlogin),
    path('student/', views.student),
    path('studentreg/', views.studentreg)

]
