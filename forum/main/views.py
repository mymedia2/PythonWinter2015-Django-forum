from django.shortcuts import render

from django.http import HttpResponseRedirect
from main.models import Message

def forum(request):
    if request.method == 'POST' and 'send' in request.path_info:
        msg = Message()
        msg.text = request.POST.get('text', '')
        if request.user.is_authenticated():
            msg.author = request.user
        msg.save()
        return HttpResponseRedirect("/forum")
    messages = Message.objects.all()
    return render(request, 'forum.html', {'messages': messages})
