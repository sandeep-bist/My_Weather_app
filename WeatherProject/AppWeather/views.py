from django.shortcuts import render,redirect,get_object_or_404
import requests
import string
from .models import City
from .forms import CityForm
from django.contrib import messages

api_id = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2d3f42fa4ba94ecf0d746e9341b37881'


def TemperatureView(request):

    if request.method == "POST":
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['city']
            city_count = City.objects.filter(city=new_city).count()
            if city_count == 0:
                result = requests.get(api_id.format(new_city)).json()

                if result["cod"] == 200:
                    messages.success(request,"City Added Successfully")
                    form.save()
                else:
                    messages.error(request,"City not found",extra_tags='danger')
            # elif city_count ==1:
            #     messages.error(request, "City Already Exist", extra_tags='danger')
            #     result = requests.get(api_id.format(new_city)).json()
            #     form.save()

            else:
                messages.error(request,"City Already Exist",extra_tags='danger')


    form= CityForm()
    cities = City.objects.all()
    weather_detail=[]
    for city in cities:
        response = requests.get(api_id.format(city))
        details= response.json()
        # print(details)
        weather={
            'city' : city,
            'description': details['weather'][0]['description'],
            'temp': details['main']['temp'],
            'temp_min': details['main']['temp_min'],
            'temp_max': details['main']['temp_max'],
            'description':details['weather'][0]['description'],
            'icon':details['weather'][0]['icon'],
            'country':details['sys']['country'],
            'speed': details['wind']['speed'],
          }
        weather_detail.append(weather)
    context={"weather_detail":weather_detail,"form":form}
    return render(request,'temp.html',context)




def DeleteCity(request,id):
    city = City.objects.get(id=id)
    get_object_or_404(City,id=id).delete()
    messages.success(request, f"{city} Removed")
    return redirect('temp')


def CityDetail(request, city):
    findCity=get_object_or_404(City,city=city)
    details = requests.get(api_id.format(findCity)).json()
    print (details)

    weather = {
        'city': city,
        'description': details['weather'][0]['description'],
        'main': details['weather'][0]['main'],
        'temp': details['main']['temp'],
        'pressure': details['main']['pressure'],
        'humidity': details['main']['humidity'],
        'temp_min': details['main']['temp_min'],
        'temp_max': details['main']['temp_max'],
        'icon': details['weather'][0]['icon'],
        'country': details['sys']['country'],
        'lon': details['coord']['lon'],
        'lat': details['coord']['lat'],
        'base': details['base'],
        # 'visibility': details['visibility'],
        'speed': details['wind']['speed'],
        'clouds': details['clouds']['all'],
        'dt': details['dt'],
        'sunrise': details['sys']['sunrise'],
        'sunset': details['sys']['sunset'],
        'timezone': details['timezone'],
        'id': details['id'],
        'cod': details['cod'],  # 'deg': details['wind']['deg'],
    }
    context= {'weather':weather}
    return render(request,'city.html',context)

# def Favorite(request,city):
#
#     fav= get_object_or_404(City,city=city)
#     if fav.is_favorite:
#         fav.is_favorite = False
#     else:
#         fav.is_favorite = True
#     fav.save()
#     context={"fav":fav}
#     return render(request,'temp.html',context)
#
