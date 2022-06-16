from django.urls import path
from . import views

app_name = 'crud_main'
urlpatterns = [
    path('create_server', views.index, name="create_server"),path('create_type_of_server', views.itype_of_server, name="type_of_server"),
    path('users', views.iusers, name='users'),
    path('servers', views.iservices, name='servers'),
    path('applications', views.iapplications, name="applications"),
    path('apphasservices', views.iapphasservices, name= "apphasservices"),
    path('overall', views.ioverall, name = "overall"),
    
    path('', views.getData, name = "dataView"),

    path('update_server/<str:pk>', views.updateServer, name = "update_server"),
    path('update_type_of_server/<str:pk>', views.updateTypeOfServer, name = "update_type_of_server"),
    path('update_users/<str:pk>', views.updateUsers, name = "update_users"),
    path('update_services/<str:pk>', views.updateServices, name = "update_servers"),
    path('update_applications/<str:pk>', views.updateApplications, name = "update_applications"),
    path('update_app_has_services/<str:pk>', views.updateapphasservices, name= "update_app_has_services" ),
    path('update_overall/<str:pk>', views.updateOverall, name = "update_overall"),

    path('delete_server/<str:pk>', views.deleteServer, name="delete_server"),
    path('delete_type_of_server/<str:pk>', views.deleteTypeofserver, name="delete_type_of_server"),
    path('delete_users/<str:pk>', views.deleteUsers, name="delete_users"),
    path('delete_services/<str:pk>', views.deleteServices, name="delete_servers"),
    path('delete_applications/<str:pk>', views.deleteApplications, name="delete_applications"),
    path('delete_app_has_services/<str:pk>', views.deleteapphasservices, name = "delete_app_has_services"),
    path('delete_overall/<str:pk>', views.deleteOverall, name="delete_overall"),
    ]
