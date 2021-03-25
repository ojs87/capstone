from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items', views.items, name='items'),
    path('quests/<str:quest>', views.quests, name='quests'),

    # API Routes
    path('itemroute', views.itemroute, name='itemroute'),
    path('questroute', views.questroute, name='questroute')
]
