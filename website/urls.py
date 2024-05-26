from django.urls import path
from  website.views import index, post_details

urlpatterns = [
    path('',index, name='index'),
    path('<slug:slug>/',post_details , name='post_details')
]
