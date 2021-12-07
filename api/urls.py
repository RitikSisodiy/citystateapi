
from django.urls import path
from .import views
urlpatterns = [
    path('state/',views.stateView,name='state'),
    path('city/',views.cityView,name='city'),
    path('country/',views.countryView,name='country'),
]
