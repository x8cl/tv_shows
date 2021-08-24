from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import *
from django.contrib import messages

# Create your views here.
def root(request):
    return redirect("/shows")

def home(request):
    context = {
        "show" : Show.objects.all(),
    }
    return render(request, "tv_shows/shows.html", context)

def new_show(request):
    context = {
        "networks" : Network.objects.all()
    }
    return render(request, "tv_shows/new.html", context)

def create_show(request):
    if request.method == "GET":
        return redirect("/shows/new")
    elif request.method == "POST":
        # pasar los datos al método que escribimos y guardar la respuesta en una variable llamada errores
        errors = Show.objects.basic_validator(request.POST)
        # compruebe si el diccionario de errores tiene algo en él
        if len(errors) > 0:
            # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
            for key, value in errors.items():
                messages.error(request, value)
            # imprimo en la consola para revisar los datos
            #print(request.POST["release_date"])
            #print(str(datetime.date.today()))
            # redirigir al usuario al formulario para corregir los errores
            return redirect("/shows/new")
        else:
            title = request.POST["title"]
            description = request.POST["description"]
            networks = request.POST["networks"]
            release_date = request.POST["release_date"]
            obj = Show.objects.create(title=title, networks_id=networks, release_date=release_date, description=description)
            obj.save()
            messages.success(request, "Show created successfully!!!")
            return redirect(f"/shows/{obj.id}")

def edit_show(request, show_id):
    context = {
        "show" : Show.objects.get(id=show_id),
        "networks" : Network.objects.all().exclude(shows__id=show_id)
    }
    return render(request, "tv_shows/edit.html", context)

def update_show(request, show_id):
    if request.method == "GET":
        return redirect("/shows")
    elif request.method == "POST":
        show = Show.objects.get(id=show_id)
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/shows/{show.id}")
        else:
            new_network_id = request.POST['networks']
            new_network = Network.objects.get(id=new_network_id)

            show.title = request.POST["title"]
            show.description = request.POST["description"]
            show.networks = new_network
            show.release_date = request.POST["release_date"]
            show.save()
            print(show.networks.id)
            print(request.POST["networks"])
            messages.success(request, "Show updated successfully!!!")

            return redirect(f"/shows/{show.id}")


def delete_show(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect("/")

def show(request, show_id):
    context = {
        #"show" : Show.objects.get(id=show_id)
        "show" : get_object_or_404(Show, id=show_id)
    }
    return render(request, "tv_shows/show.html", context)

###Networks###

def networks(request):
    context = {
        "network" : Network.objects.all()
    }
    return render(request, "tv_shows/networks.html", context)

def new_network(request):
    return HttpResponse(f"placeholder for new network form")

def create_network(request):
    pass

def edit_network(request, network_id):
    return HttpResponse(f"edit network id={network_id}")

def update_network(request, show_id):
    return HttpResponse(f"update network id={show_id}")

def delete_network(request, network_id):
    return HttpResponse(f"delete network id={network_id}")

def network(request, network_id):
    context = {
        "network" : get_object_or_404(Network, id=network_id)
    }
    return render(request, "tv_shows/network.html", context)