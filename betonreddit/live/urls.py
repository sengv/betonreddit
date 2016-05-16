from django.conf.urls import url


from .views import live_main


urlpatterns = [

    url(r'^$', live_main, name="live_main"),




]
