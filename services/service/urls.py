from django.urls import path
from . import views
urlpatterns = [
    path('price', views.PriceView.as_view(), name='price'),
    path('separator', views.Separator.as_view(), name='separator'),
    path('create', views.CreatePerson.as_view(), name='person'),
]