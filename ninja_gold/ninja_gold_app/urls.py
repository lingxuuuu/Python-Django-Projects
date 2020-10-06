from django.urls import path    

from . import views

urlpatterns = [
    path('', views.index),	 
    path('process_money', views.add_money), 
    path('my_gold', views.my_gold),
    path('reset', views.reset),
   ]