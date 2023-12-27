from django.shortcuts import render
from visitors.forms import VisitorsForm

def register_visitor(request):
    form = VisitorsForm()
    context =  {
        "page_name":"Register Visitor",
        "form": form
    }
    return render(request, "registrar_visitante.html", context)
