from django.shortcuts import render
from visitors.models import Visitor
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    
    all_visitors = Visitor.objects.order_by(
        "-arrival_time"
    )
    visitors_waiting = all_visitors.filter(
        status="WAITING"
    )
    visitors_visiting = all_visitors.filter(
        status="VISITING"
    )
    visitors_finished = all_visitors.filter(
        status="LEAVE"
    )
    actual_time = timezone.now()
    actual_month = actual_time.month
    visitors_month = all_visitors.filter(
        arrival_time__month= actual_month
    )
    
    context = {
        "page_name": "Dashboard homepage",
        "visitors_list": all_visitors,
        "visitors_quantity": visitors_month.count(),
        "visitors_wait": visitors_waiting.count(),
        "visitors_visit": visitors_visiting.count(),
        "visitors_leave": visitors_finished.count()
    }
    
    return render(request, "index.html", context)
