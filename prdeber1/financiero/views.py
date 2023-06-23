from django.shortcuts import render
from financiero.models import EntidadFinanciera

# Create your views here.
def bancos(request):
    mis_bancos = EntidadFinanciera.objects.all()
    num_bancos = len(mis_bancos)
    informacion_template = {"mis_entidades":mis_bancos, "num_entidades":num_bancos}
    return render(request, "bancos.html", informacion_template)


