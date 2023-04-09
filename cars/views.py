from django.shortcuts import render
from cars.models import Car

# Create your views here.

def index(request):
    number = request.POST.get('number')
    car = None
    if number:
        try:
            car = Car.objects.get(number=number)
        except Car.DoesNotExist:
            pass
    return render(request, 'index.html', {'number': number, 'car': car})