from django.conf.urls import url 
from . import views 
 
app_name = "api"
urlpatterns = [ 
    url(r'^organziations$', views.org),
    url(r'^organizations_all$', views.org_list),
]