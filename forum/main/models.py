from django.db import models

class MessageManager(models.Manager):
    def create_message(self, text):
        return Message(text=text)

class Message(models.Model):
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    objects = MessageManager()
