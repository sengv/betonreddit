from django.http import HttpResponse
from django.views.generic import View

from django.shortcuts import render

from . import subreddit

class redApi(View):
    def get(self, request, *args, **kwargs):
        sub = subreddit.subreddit(kwargs.get('sub'))
        sub.loadData()
        if sub.posts:
            return render(request, "subdata.html", {'posts':sub.posts})
        return HttpResponse('Error getting subreddit data')
        