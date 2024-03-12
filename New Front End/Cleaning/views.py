# from django.shortcuts import render
# from .models import CleaningStatus

# # Create your views here.
# def Cleaning_Status(request):
#     return render(request,'Cleaning_Management.html')
from django.shortcuts import render
from django.http import JsonResponse
from .models import MarkedDate
from datetime import datetime

def calendar_view(request):
    marked_dates = MarkedDate.objects.all()
    return render(request, 'Cleaning_Management.html', {'marked_dates': marked_dates})

def get_marked_dates(request):
    marked_dates = list(MarkedDate.objects.values('date', 'cleaned'))
    # return JsonResponse({'marked_dates': marked_dates})
    return render(request, 'Cleaning_Management.html', {'marked_dates': marked_dates})

def mark_date(request):
    if request.method == 'POST':
        date_str = request.POST.get('date')
        cleaned = request.POST.get('cleaned') == 'true'
        date = datetime.strptime(date_str, "%d-%m-%y").date()
        MarkedDate.objects.update_or_create(date=date, defaults={'cleaned': cleaned})
        # return JsonResponse({'status': 'ok'})
        return render(request, 'Cleaning_Management.html')
    return JsonResponse({'status': 'error'})



