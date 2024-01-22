from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    text = models.TextField()
    folder_id = models.ForeignKey(
        "Folder", on_delete=models.CASCADE, null=True,  blank=True, related_name="notes"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.text


class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="folders")
    title = models.CharField(max_length=100)
    colour = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
