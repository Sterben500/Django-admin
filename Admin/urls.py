from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_server/', create_server),
]
