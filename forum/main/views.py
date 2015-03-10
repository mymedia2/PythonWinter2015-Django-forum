# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from main.models import Message

def forum(request):
    if request.method == 'POST' and 'send' in request.path_info:
        # TODO: выделить этот код в отдельную функцию
        text = request.POST.get('text')
        if not text:
            # NOTE: некрасиво
            return HttpResponseRedirect(reverse(forum) + "?err=empty-msg")
        msg = Message()
        msg.text = text
        if request.user.is_authenticated():
            msg.author = request.user
        msg.save()
        return HttpResponseRedirect(reverse(forum))
    context = {'messages': Message.objects.all()}
    if request.GET.get('err') == 'empty-msg':
        context['errors'] = 'You can not send the empty message'
    return render(request, 'forum.html', context)
