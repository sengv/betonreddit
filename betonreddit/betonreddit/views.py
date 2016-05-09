from django.shortcuts import render




#Make the home_files return the appropriate humans.txt and robots.txt? What do they even do
def home_files(request):
    return render(request, "<p>Work in Progress<p>", {})
    
    
    
def home(request):
    return render(request, "index.html", {})