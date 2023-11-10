
from django.urls import path
from . import views
app_name='MOVIEAPP'# for using namespace in a link
urlpatterns = [
  
    path('', views.Index,name='index'),
    path('movie/<int:movie_id>/', views.detail,name='detail'),
    path('add/', views.add_movie,name='add_movie'),
    path('update/<int:id>/', views.update,name='updates'),
    path('delete/<int:id>/', views.delete,name='delete'),
]