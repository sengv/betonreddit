from django.shortcuts import render
from django.http import HttpResponse



#Make the home_files return the appropriate humans.txt and robots.txt? What do they even do
def home_files(request):
    return HttpResponse("<p>In progress</p>")
    
    
    
def home(request):
    return render(request, "index.html", {})
    
    
    
def instructions(request):
    
    return render(request, "betonreddit/instructions.html", {})