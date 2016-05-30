from django.shortcuts import render


from wager.models import Wager, Betline

# Create your views here.


def history_main(request):

    try:
        
        if request.user.is_authenticated():
            print("AUTHENTICATO X")
        else:
            print("NOT AUTHENTICATED")
        
    except:
        print("something went wrong. except.")
        pass

        
    context_dict = {}
    
    all_wagers = Wager.objects.all()
    
    context_dict['all_wagers'] = Wager.objects.all()
    
    
    #Once we can authenticate a user, we can fetch their wagers.
    #context_dict['all_wagers'] = Wager.objects.filter(email=request.user.email)
    
    return render(request, "betonreddit/history.html", context_dict)
    
    


