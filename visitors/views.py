from django.shortcuts import render

def register_visitor(request):
    context =  {}
    return render(request, "registrar_visitante.html", context)
