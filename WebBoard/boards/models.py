from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=225, unique=True)
    last_update = models.DateField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.SET('deleted user'))

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=400)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.SET('deleted user'))
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.SET('deleted user'))


