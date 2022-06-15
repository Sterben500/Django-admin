from django.urls import path, include
from . import views

app_name= 'crud_main/templates'

urlpatterns = [
    path('index', views.index, name="index"),

    path('server', views.iserver, name="server"),
    path('type_of_server', views.itype_of_server, name="type_server"),
    path('users', views.iusers, name='users'),
    path('servers', views.iservices, name='servers'),
    path('applications', views.iapplications, name="applications"),
    path('apphasservices', views.iapphasservices, name= "apphasservices"),
    path('overall', views.ioverall, name = "overall"),
    
    path('getData', views.getData, name = "dataView"),

    path('update_server/<str:pk>', views.updateServer, name = "Update_serv"),
    path('update_type_of_server/<str:pk>', views.updateTypeOfServer, name = "Update_type_serv"),
    path('update_users/<str:pk>', views.updateUsers, name = "Update_users"),
    path('update_services/<str:pk>', views.updateServices, name = "Update_servers"),
    path('update_applications/<str:pk>', views.updateApplications, name = "Update_applications"),
    path('update_app_has_services/<str:pk>', views.updateapphasservices, name= "Update_apphasservices" ),
    path('update_overall/<str:pk>', views.updateOverall, name = "Update_overall"),

    path('delete_server/<str:pk>', views.deleteServer, name="Delete_serv"),
    path('delete_type_of_server/<str:pk>', views.deleteTypeofserver, name="Delete_type_serv"),
    path('delete_users/<str:pk>', views.deleteUsers, name="Delete_users"),
    path('delete_services/<str:pk>', views.deleteServices, name="Delete_servers"),
    path('delete_applications/<str:pk>', views.deleteApplications, name="Delete_applications"),
    path('delete_app_has_services/<str:pk>', views.deleteapphasservices, name = "Delete_apphasservices"),
    path('delete_overall/<str:pk>', views.deleteOverall, name="Delete_overall"),

    path('search/', views.search, name="Search"),
    ]
