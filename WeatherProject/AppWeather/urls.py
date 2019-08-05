from django.urls import path
from . import views

urlpatterns = [
    path('',views.TemperatureView,name='temp'),
    path('delete/<int:id>',views.DeleteCity,name='delete'),
    path('<city>',views.CityDetail,name='detail'),
    # path('<city>/favorite',views.Favorite,name='favorite'),
]