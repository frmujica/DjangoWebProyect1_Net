from django.urls import path

from ordenes import views

urlpatterns = [
    path('ordenes/', views.nuevos, name="nuevos"),
    path('ordenes/nuevos/', views.nuevos, name="nuevos"),
    path('ordenes/manifestados/', views.manifestados, name="manifestados"),
    path('ordenes/archivados/', views.archivados, name="archivados"),
    path('ordenes/seguimiento/', views.seguimiento, name="seguimiento"),
    #path('setup/<str:value>/', views.setuprefrehs, name="setuprefrehs"),
]
