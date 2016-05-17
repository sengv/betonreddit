from django.conf.urls import url


from .views import highscore_main


urlpatterns = [

    url(r'^$', highscore_main, name="highscore_main"),

]
