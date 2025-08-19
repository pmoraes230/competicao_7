from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("home/", views.home, name="home"),
    path("deteils_event/<int:id_event>/", views.deteils_event, name="deteils_event"),
    path("buy_ticket/<int:id_event>/", views.buy_ticket, name="buy_ticket"),
    path("ticket_generate/<str:id_ticket>/", views.ticket_generate, name="ticket_generete"),
    path("list_ticket/", views.ticket_list, name="ticket_list")
]
