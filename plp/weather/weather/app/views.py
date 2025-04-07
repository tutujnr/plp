from django.shortcuts import render
import requests
from .forms import CityForm
from .models import City

# Create your views here.

def index(request):
    weather_data = None
    error = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = 'YOUR_API_KEY'
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }

                # Save to DB
                City.objects.create(
                    name=weather_data['city'],
                    temperature=weather_data['temperature'],
                    description=weather_data['description'],
                    icon=weather_data['icon']
                )
            else:
                error = "City not found."
    else:
        form = CityForm()

    recent_searches = City.objects.order_by('-searched_at')[:5]

    return render(request, 'index.html', {
        'form': form,
        'weather': weather_data,
        'error': error,
        'recent_searches': recent_searches
    })
