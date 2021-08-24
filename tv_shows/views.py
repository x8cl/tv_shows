from django.shortcuts import redirect, render, HttpResponse
from .models import *
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
        "network" : Network.objects.all()
    }
    return render(request, "tv_shows/new.html", context)

def create_show(request):
    if request.method == "GET":
        return redirect("/shows/new")
    elif request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        network = request.POST["network"]
        release_date = request.POST["release_date"]
        obj = Show.objects.create(title=title, networks_id=network, release_date=release_date, description=description)
        obj.save()
        return redirect(f"/shows/{obj.id}")

def edit_show(request, show_id):
    context = {
        "show" : Show.objects.get(id=show_id),
        "network" : Network.objects.all().exclude(shows__id=show_id)
    }
    return render(request, "tv_shows/edit.html", context)

def update_show(request, show_id):
    if request.method == "GET":
        return redirect("/shows")
    elif request.method == "POST":
        new_title = request.POST["title"]
        new_description = request.POST["description"]
        new_network = request.POST["network"]
        new_release_date = request.POST["release_date"]

        show = Show.objects.get(id=show_id)

        show.title = new_title
        show.description = new_description
        show.network = new_network
        show.release_date = new_release_date
        show.save()

        return redirect(f"/shows/{show.id}")


def delete_show(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect("/")

def show(request, show_id):
    context = {
        "show" : Show.objects.get(id=show_id)
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
        "network" : Network.objects.get(id=network_id)
    }
    return render(request, "tv_shows/network.html", context)