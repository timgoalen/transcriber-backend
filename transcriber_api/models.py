from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    note = models.TextField()
    timestamp = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True, blank = True)
    # user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    # class Meta:
    #     ordering = ["-created_on"]
    
    def __str__(self):
        return self.note
