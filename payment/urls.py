from django.urls import path

from . import views


urlpatterns = [
    path('make', views.addpayment, name='add-payment'),
    path('confirm', views.makepayment, name='confirm-payment'),
    path('insert', views.insertpayment, name='insert-payment')
   
]
