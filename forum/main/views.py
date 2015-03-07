from django.shortcuts import render

from main.models import Message

def forum(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        msg = Message.objects.create_message(text)
        msg.save()
    messages = Message.objects.all()
    return render(request, 'forum.html', {'messages': messages})
