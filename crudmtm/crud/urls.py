
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud_main.urls')),
    path('crud_main', include('crud_main.urls'))
   


]
