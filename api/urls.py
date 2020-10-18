from django.conf.urls import url 
from . import views

 
app_name = "api"
urlpatterns = [ 
    url('organizations/', views.org.as_view()),
    url('organizations_all/', views.org_list.as_view()),
]