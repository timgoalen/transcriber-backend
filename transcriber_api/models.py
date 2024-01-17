from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    # id = models.IntegerField()
    text = models.TextField()
    folder_id = models.CharField(max_length=25)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True)
    # user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.note


class Folder(models.Model):
    title = models.CharField(max_length=100)
    colour = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True)
    # user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)


    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.note
