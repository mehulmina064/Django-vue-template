"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView


from django.contrib import admin
from django.urls import  path,include
from rest_framework.schemas import get_schema_view


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='project/spa.html'), name='main-home'),
    # path('login', TemplateView.as_view(template_name='project/spa.html'), name='login'),

    #auth apps urls
    path("", include("apps.authentication.urls")), # Auth routes - login / register


    #urls of home application
    path("", include("apps.home.urls")),   

    # urls of organization application
    path('api', include('apps.authentication.apis.urls')),
    path('o/', include('apps.organizations.urls')),


    #urls of account application
    

    path ('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # #path for api schema
    # path('api_schema/', get_schema_view(
    #     title="Prodo Api",
    #     description="API developers Hpoing to use our service"
    # ), name='api_schema'),

    #path for swagger ui
    

    #jwt token paths
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

 
]

