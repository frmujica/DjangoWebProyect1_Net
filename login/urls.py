from django.urls import path

from login import views

urlpatterns = [
    path('acceso/', views.acceso, name="acceso"),
    path('acceso/listadousuarios/', views.listaUsuarios, name="listadousuarios"),
    #path('setup/<str:value>/', views.setuprefrehs, name="setuprefrehs"),
]
