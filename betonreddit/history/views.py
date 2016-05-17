from django.shortcuts import render

# Create your views here.


def history_main(request):
    
    return render(request, "betonreddit/history.html", {})