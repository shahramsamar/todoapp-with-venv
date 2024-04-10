from django.urls import path
from website  import views



app_name='website'

urlpatterns =[
    path('', views.index),
    path('about',views.about),
    path('contact',views.contact),
]