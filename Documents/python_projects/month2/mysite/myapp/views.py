from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from myapp.models import Car


class CarsList(ListView):
    model = Car
    template_name = "myapp/list.html"
    context_object_name = "cars"
class CarDetail(DetailView):
    model = Car
    template_name = "myapp/detail.html"
    context_object_name = "car"

class CreateCar(CreateView):
    model = Car
    template_name = "myapp/create.html"
    fields = ["name", "brand", "horse_power", "capacity", "description", "color", "price", "car_image"]
    success_url = reverse_lazy('cars')
class UpdateCar(UpdateView):
    model = Car
    template_name = "myapp/update.html"
    fields = ["name", "brand", "horse_power", "capacity", "description", "color", "price", "car_image"]
    success_url = reverse_lazy("cars")
class DeleteCar(DeleteView):
    model = Car
    template_name = "myapp/delete.html"
    success_url = reverse_lazy("cars")