from django.urls import path, include
from rest_framework import routers

from station.views import (bus_list,
                           bus_detail, BusList,
                           BusDetail, BusListGen,
                           BusDetailGen, BusListGeneric,
                           BusDetailGeneric, BusListSet, BusDetailSet, BusViewSet, BusViewSetModel)


bus_list = BusViewSet.as_view(
    actions={"get": "list", "post": "create"}
)

bus_detail = BusViewSet.as_view(
        actions={
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"}
)

router = routers.DefaultRouter()
router.register("buses", BusViewSetModel)


# urlpatterns = [
#     path("buses/", bus_list, name="bus-list"),
#     path("buses/<int:pk>/", bus_detail, name="bus-detail"),
# ]

urlpatterns = [
    path("", include(router.urls))
]

app_name = "station"
