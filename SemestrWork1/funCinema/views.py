from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Actor
from .models import Serials
from .forms import Form, UserRegisterForm



class SerialsView(View):
    def get(self, request):
        serials = Serials.objects.all()
        return render(request, "serials/serials_list.html", {"serials": serials})


class SerialDetailView(View):
    def get(self, request):
        serials = Serials.objects.all()
        return render(request, "serials/single_serial.html", {"serials": serials})


class SingleSerial(View):
    def get(self, request, id):
        serial = get_object_or_404(Serials, id=id)
        return render(request, "serials/detail_serial.html", {"serial": serial})


class ActorView(View):
    def get(self, request, id):
        serial = get_object_or_404(Actor, id=id)
        return render(request, "serials/actor.html", {"serial": serial})


def add_list(request):
    context = {'list': Serials.objects.all()}
    return render(request, 'serials/mySerial.html', context)



def serials_form(request):
    if request.method == "GET":
        form = Form()
        return render(request, 'serials/serials_form.html', {'form': form})
    else:
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list/')


def delete_list(request):
    return


def serials_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = Form()
        else:
            serials = Serials.objects.get(pk=id)
            form = Form(instance=serials)
        return render(request, 'serials/serials_form.html', {'form': form})
    else:
        if id == 0:
            form = Form(request.POST)
        else:
            serials = Serials.objects.get(pk=id)
            form = Form(request.POST, instance=serials)
        if form.is_valid():
            form.save()
        return redirect('/list/')


def delete_list(request, id):
    serials = Serials.objects.get(pk=id)
    serials.delete()
    return redirect('/list/')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('serials_list')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
