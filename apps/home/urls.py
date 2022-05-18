from django.urls import path,include, re_path
from apps.home import views



urlpatterns = [
    
    # path('', views.home.as_view(), name='home'),
    path('', views.index, name='home'),
   	
    
    # Matches any html 
    re_path(r'^.*\.', views.pages, name='pages'),
    

]

