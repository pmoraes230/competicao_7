from django.urls import path
from . import views

urlpatterns = [
    path("validador/", views.validador, name="validador"),
    path("ticket_cancel/<str:id_ticket>/", views.ticket_cancel, name="ticket_cancel")
]
