from django.urls import path

from login import views

urlpatterns = [
    path('acceso/', views.acceso, name="acceso"),
    path('acceso/listadousuarios/', views.listaUsuarios, name="listadousuarios"),
    path('acceso/editarusuario/<str:id>/', views.editarusuario, name="editarusuario"),
    path('acceso/actualizarusuario/', views.actualizarusuario, name="actualizarusuario"),
    
    #path('setup/<str:id>/', views.setuprefrehs, name="setuprefrehs"),
]
