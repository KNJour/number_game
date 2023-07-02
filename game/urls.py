from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("attempt", views.attempt),
    path("reset", views.reset)
	]