from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('exercise', views.exercise, name='exercise'),
    path('makeinvoice', views.makeinvoice, name='makeinvoice'),
    #re_path(r'^$', 'invoice.views.exercise', name='exercise'),
]
