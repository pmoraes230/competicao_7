from django.shortcuts import render, redirect
from django.contrib import messages
from home.views import get_user_profile
from home import models
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
import numpy as np
import base64
import io

# Create your views here.
def dashboard(request):
    context = get_user_profile(request)
    
    event = None
    sectors = None
    types_of_sectors = []
    grafic_sectors = []
    
    if request.method == "POST":
        name_input = request.POST.get("name_input")
        if not name_input:
            messages.info(request, "Insira um nome no campo antes de pesquisar")
            return redirect("dash")
        
        try:
            event = models.Event.objects.get(event_name=name_input)
            sectors = models.Sector.objects.filter(event=event)
            types_of_sectors = [sector.name for sector in sectors]
            tickets = models.Ticket.objects.filter(event=event)
            
            issued_by_sector = {t: tickets.filter(sector__name=t, status='emitido').count() for t in types_of_sectors}
            validation_by_sector = {t: tickets.filter(sector__name=t, status='validado').count() for t in types_of_sectors}
            sector_capacity = {sector.name: sector.limit_ticket for sector in sectors}
            
            for name_sector in types_of_sectors:
                labals = [f"Capacidade ({name_sector})", f"Emitido ({name_sector})", f"Validados ({name_sector})"]
                data = [sector_capacity[name_sector], issued_by_sector[name_sector], validation_by_sector[name_sector]]
                filtered_labels = [labals[i] for i in range(len(data)) if data[i] > 0]
                filtered_data = [d for d in data if d > 0]
                
                if filtered_data:
                    fig, ax = plt.subplots(figsize=(6,4))
                    colors = ['#F31366', '#1331A1', '#A2CA02'][:len(filtered_data)]
                    
                    x_pos = np.arange(len(filtered_data))
                    bars = ax.bar(x_pos, filtered_data, color=colors)
                    
                    ax.set_xticks(x_pos)
                    ax.set_xticklabels(filtered_labels, rotation=30, ha='right')
                    
                    for bar in bars:
                        height = bar.get_height()
                        ax.annotate(f'{height}',
                                    xy=(bar.get_x() + bar.get_width() / 2, height),
                                    xytext=(0,3),
                                    textcoords="offset points",
                                    ha='center', va='bottom')
                        
                    plt.tight_layout()
                    
                    buf = io.BytesIO()
                    plt.savefig(buf, format='png', bbox_inches='tight')
                    plt.close(fig)
                    grafic_base64 = base64.b64encode(buf.getbuffer()).decode('utf-8')
                    buf.close()
                    
                    grafic_sectors.append({'sector': name_sector, 'grafic': grafic_base64})
                                
        except models.Event.DoesNotExist:
            messages.error(request, "Evento não encontrado")
            return redirect("dash")
    
    context.update({
        'event': event,
        'type_sector': types_of_sectors,
        'grafic_sector': grafic_sectors
    })
    
    return render(request, "dash.html", context)