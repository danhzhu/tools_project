from django.urls import path
from . import views

urlpatterns = [
        path('', views.all_squirrels),
        path('<str:unique_squirrel_id>/', views.edit_squirrels),
        ]
