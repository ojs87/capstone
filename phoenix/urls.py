from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items', views.items, name='items'),
    path('quests/<str:quest>', views.quests, name='quests'),
    path('foundinraid', views.foundinraid, name='foundinraid'),

    # API Routes
    path('itemroute', views.itemroute, name='itemroute'),
    path('questroute', views.questroute, name='questroute')
]
