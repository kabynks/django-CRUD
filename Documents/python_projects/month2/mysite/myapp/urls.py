from django.urls import path

from myapp.views import *

urlpatterns = [
    path('', CarsList.as_view(), name="cars"),
    path("cars/<int:pk>/", CarDetail.as_view(), name="car"),
    path("cars/create_car/", CreateCar.as_view(), name="create_car"),
    path("car_update/<int:pk>/", UpdateCar.as_view(), name="update_car"),
    path("car_delete/<int:pk>/", DeleteCar.as_view(), name="delete_car"),
]