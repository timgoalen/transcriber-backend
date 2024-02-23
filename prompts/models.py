from django.db import models
from django.contrib.auth.models import User


class Prompt(models.Model):
    """
    MODEL: database for Prompt objects.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="prompts")
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.text
