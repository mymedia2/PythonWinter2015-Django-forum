from django.db import models

from django.contrib.auth.models import User

class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, db_index=False, null=True, on_delete=models.SET_NULL)
    datetime = models.DateTimeField(auto_now_add=True)
