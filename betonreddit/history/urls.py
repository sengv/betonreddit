from django.conf.urls import url


from .views import history_main


urlpatterns = [

    url(r'^$', history_main, name="history_main"),




]
