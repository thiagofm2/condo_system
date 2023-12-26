from django.shortcuts import render
from visitors.models import Visitor

def index(request):
    
    all_visitors = Visitor.objects.all()
    
    context = {
        "page_name": "Dashboard homepage",
        "visitors_list": all_visitors
    }
    
    return render(request, "index.html", context)
