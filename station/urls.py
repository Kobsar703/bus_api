from django.urls import path

from station.views import bus_list, bus_detail, BusList, BusDetail, BusListGen, BusDetailGen

urlpatterns = [
    path("buses/", BusListGen.as_view(), name="bus-list"),
    path("buses/<int:pk>/", BusDetailGen.as_view(), name="bus-detail"),
]

app_name = "station"
