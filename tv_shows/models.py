from django.db import models
from django.db.models.base import Model

# Create your models here.
class Network(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
    
    def __str__(self):
        return self.name
    
class Show(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    release_date = models.DateField()
    networks = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title