from django.shortcuts import render

# Create your views here.



def live_main(request):
    
    return render(request, "betonreddit/live.html", {})