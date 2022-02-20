from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='index'),
    path("v1/", views.v1, name='index'),
    path("display/<int:id>/", views.display, name='index'),
    path("create/", views.create, name='index'),
]