from django.urls import path 
from . import views

app_name = 'pdfmr'

urlpatterns = [
    path('top',views.top, name='top')
]