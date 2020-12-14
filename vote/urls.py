from django.urls import path


from .views import *

app_name = 'vote'

urlpatterns = [
    path('', index, name='index'),
    path('<str:pk>/', detail, name='detail'),
    path('<str:pk>/result/', result, name='result'),
    path('<str:pk>/vote/', vote, name='vote'),
]
