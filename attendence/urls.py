from . import views
from django.urls import path

urlpatterns = [
    path('attend/', views.attend),
    path('detail/', views.detail),
    path('attend2/',views.attend2),
    path('detail2/',views.detail2),
    path('allstudent/', views.allstudent),
    path("edit/<int:id>", views.edit),
    path('edit2/', views.edit2),
    path('deldata/<int:id>',views.deldata),
    path('info/<int:id>', views.info)

]