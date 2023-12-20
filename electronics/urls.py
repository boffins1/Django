from django.urls import path
from .views import gadjets,read,home
urlpatterns=[
    path('gadjets/',gadjets),
    path('read/<int:id>/',read),
    path('home/',home),
]