from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("deteils_event/<int:id_event>/", views.deteils_event, name="deteils_event"),
    path("buy_ticket/<int:id_event>/", views.buy_ticket, name="buy_ticket")
]
