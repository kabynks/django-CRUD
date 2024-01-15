from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from myapp.models import Car


class CarsList(ListView):
    model = Car
    template_name = "myapp/list.html"
    context_object_name = "cars"
class CarDetail(LoginRequiredMixin,DetailView):
    model = Car
    template_name = "myapp/detail.html"
    context_object_name = "car"

class CreateCar(LoginRequiredMixin,CreateView):
    model = Car
    template_name = "myapp/create.html"
    fields = ["name", "brand", "horse_power", "capacity", "description", "color", "price", "car_image"]
    success_url = reverse_lazy('cars')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateCar(LoginRequiredMixin,UpdateView):
    model = Car
    template_name = "myapp/update.html"
    fields = ["name", "brand", "horse_power", "capacity", "description", "color", "price", "car_image"]
    success_url = reverse_lazy("cars")
class DeleteCar(LoginRequiredMixin,DeleteView):
    model = Car
    template_name = "myapp/delete.html"
    success_url = reverse_lazy("cars")

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    context_object_name = "signup"
    success_url = reverse_lazy("login")
def my_cars(request):
    cars = Car.objects.filter(author=request.user)
    context = {
        "cars": cars
    }
    return render(request, "myapp/show_cars.html", context=context)
