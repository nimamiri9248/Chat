from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
   
    def __str__(self):
        self.name


class Server(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='server_owner', 
                              null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='server_category',  null=True)
    description = models.CharField(null=True, max_length=255)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='server_members')

    def __str__(self):
        self.name


class Channel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='channel_owner',
                              null=True)
    topic = models.CharField(max_length=100)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="channel_server")

    def __str__(self):
        self.name

