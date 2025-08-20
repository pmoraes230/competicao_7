from django.shortcuts import render, redirect
from django.contrib import messages
from home.views import get_user_profile
from home import models
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, base64, io

def dash(request):
    context = get_user_profile(request)
    event, grafic_sectors = None, []

    if request.method == "POST":
        try:
            event = models.Event.objects.get(event_name=request.POST.get("input_name"))
            for sector in models.Sector.objects.filter(event=event):
                # conta ingressos
                counts = {
                    "Capacidade": sector.limit_ticket,
                    "Emitido": models.Ticket.objects.filter(event=event, sector=sector, status="emitido").count(),
                    "Validado": models.Ticket.objects.filter(event=event, sector=sector, status="validado").count(),
                    "Cancelado": models.Ticket.objects.filter(event=event, sector=sector, status="cancelado").count(),
                }

                # pega só os que têm valor
                data = [v for v in counts.values() if v > 0]
                labels = [f"{k} ({sector.name})" for k,v in counts.items() if v > 0]
                if not data: continue

                # gráfico simples
                fig, ax = plt.subplots()
                bars = ax.bar(np.arange(len(data)), data, color=['#F31366','#F44528','#A2CA02','#010101'][:len(data)])
                ax.set_xticks(range(len(data)))
                ax.set_xticklabels(labels, rotation=30, ha='right')
                for bar in bars:
                    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height(), str(int(bar.get_height())),
                            ha='center', va='bottom')

                buf = io.BytesIO()
                plt.tight_layout()
                plt.savefig(buf, format="png")
                plt.close(fig)

                grafic_sectors.append({"sector": sector.name, "grafic": base64.b64encode(buf.getvalue()).decode()})

        except models.Event.DoesNotExist:
            messages.error(request, "Evento não encontrado")
            return redirect("dashboard")

    context.update({"event": event, "grafic_sectors": grafic_sectors})
    return render(request, "dash.html", context)
