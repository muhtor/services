from django.urls import path
from . import views


urlpatterns = [
    path('data', views.ParserView.as_view(), name='parser'),
]