from django.urls import path
from .views import Men,Women,read,read1
urlpatterns=[
    path('Men/',Men),
    path('Women/',Women),
    path('Men/read/<int:id>/',read),
    path('Women/read1/<int:id>/',read1)
]