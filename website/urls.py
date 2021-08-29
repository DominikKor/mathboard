from django.urls import path

from website import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:number>", views.number_dashboard, name="number_dashboard"),
]
