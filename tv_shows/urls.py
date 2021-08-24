from django.urls import path
from . import views

app_name = "tv_shows"
urlpatterns = [
    path("", views.root, name="root"),
    path("shows", views.home, name="home"),
    path("shows/new", views.new_show, name="new_show"),
    path("shows/create", views.create_show, name="create_show"),
    path("shows/<show_id>", views.show, name="show"),
    path("shows/<show_id>/edit", views.edit_show, name="edit_show"),
    path("shows/<show_id>/update", views.update_show, name="update_show"),
    path("shows/<show_id>/delete", views.delete_show, name="delete_show"),
    path("networks", views.networks, name="networks"),
    path("networks/new", views.new_network, name="new_network"),
    path("networks/<network_id>", views.network, name="network"),
    path("networks/<network_id>/edit", views.edit_network, name="edit_network"),
    path("networks/<network_id>/delete", views.delete_network, name="delete_network")
]
