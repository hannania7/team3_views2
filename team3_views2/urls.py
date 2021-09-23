"""care URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from head import survey_views
from head import main_views  
from head import chart_views  
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # main
    path('', main_views.MainFunc),
    path('main', main_views.MainFunc),
    
    path('imageinput', main_views.ImageInputFunc),
    path('imageresult', main_views.ImageResultFunc),    

    
    # survey
    path('survey',survey_views.SurveyFunc),  
    path('surveyresult',survey_views.SurveyresultFunc),  
     
    # page
    path('statistics', chart_views.Chart),
    path('healthInform', chart_views.HealthInform),
]
 