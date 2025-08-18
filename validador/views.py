from django.shortcuts import render, redirect
from django.contrib import messages
from home.views import get_user_profile
from home import models

# Create your views here.
def validation(request):
    context = get_user_profile(request)
    if request.method == "POST":
        ticket_input = request.POST.get("id_ticket")
            
        try:
            ticket = models.Ticket.objects.get(id_ticket=ticket_input)
            if ticket.status == "validado":
                messages.info(request, "Ingresso já validado antes, tente validar outro.")
                return redirect("validador")
            elif ticket.status == "cancelado":
                messages.info(request, "Ingresso cancelado para este evento, tente validar outro.")
                return redirect("validador")
            elif ticket.status == "emitido":
                ticket.status = "validado"
                ticket.save()
                messages.success(request, "Ingresso validado com sucesso.")
                return redirect("validador")
        except models.Ticket.DoesNotExist:
            messages.error(request, "Ingresso não encontrado, tente validar novamente.")
        
    return render(request, "validation.html", context)