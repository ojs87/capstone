from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items', views.items, name='items'),

    # API Routes
    path('itemroute', views.itemroute, name='itemroute'),
    path('questroute', views.questroute, name='questroute')
]
