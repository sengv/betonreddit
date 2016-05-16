from django.shortcuts import render

# Create your views here.



def highscore_main(request):
    
    return render(request, "highschore.html", {})