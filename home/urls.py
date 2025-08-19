from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("home/", views.home, name="home"),
=======
    path("", views.home, name="home"),
>>>>>>> parent of 04ffaf0 (login)
    path("deteils_event/<int:id_event>/", views.deteils_event, name="deteils_event"),
    path("buy_ticket/<int:id_event>/", views.buy_ticket, name="buy_ticket"),
    path("ticket_generate/<str:ticket_id>/", views.export_ticket_pdf, name="ticket_export"),
    path("ticket_list/", views.ticket_list, name="ticket_list")
]
