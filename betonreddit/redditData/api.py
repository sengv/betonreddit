from django.http import HttpResponse
from django.views.generic import View

from django.shortcuts import render

from . import subreddit, post

class redApi(View):
    def getSub(self, request, *args, **kwargs):
        sub = subreddit.subreddit(kwargs.get('sub'))
        sub.loadData()

        if sub.posts:
            return render(request, "subdata.html", {'posts':sub.posts})
        return HttpResponse('Error getting subreddit data')

    def getPost(self, request, *args, **kwargs):
        comments = post.post(kwargs.get('url'))
        comments.loadData()

        if comments.comments:
            return render(request, "comments.html", {'comments':comments.comments})
        return HttpResponse('Error getting subreddit data')