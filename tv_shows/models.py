from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        #creo un diccionario con los errores key/value
        errors = {}
        #valido que el campo "title" tenga al menos 2 caracteres y saco los espacios con strip
        if len(postData["title"].strip()) < 2:
            errors["title"] = "Title must be at least 2 characters"
        #valido que el campo "networks" exista
        if not postData["networks"].isdigit():
            errors["networks"] = "Please select a network"
        #valido que el campo "release_date" exista
        if len(postData["release_date"]) < 1:
            errors["release_date"] = "Please enter release date"
        #valido que el campo "release_date" sea mayor a la fecha actual
        if postData["release_date"] > str(datetime.date.today()):
            errors["release_date"] = "Release date is in the future...."
        #valido que el campo "description" tenga al menos 10 caracteres y saco los espacios con strip
        if len(postData["description"].strip()) > 0 and len(postData["description"].strip()) < 10:
            errors["description"] = "Description must be at least 10 characters (blank is OK)"
        #retorno errores
        return errors
        

class Network(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("id",)
        app_label = "tv_shows"
    
    def __str__(self):
        return self.name
    
class Show(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    release_date = models.DateField()
    networks = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    class Meta:
        ordering = ("id",)
        app_label = "tv_shows"

    def __str__(self):
        return self.title