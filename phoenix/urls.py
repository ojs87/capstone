from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('quests/<str:quest>', views.quests, name='quests'),
    path('foundinraid', views.foundinraid, name='foundinraid'),
    path('tracker', views.tracker, name='tracker'),

    # API Routes
    path('itemroute', views.itemroute, name='itemroute'),
    path('questroute', views.questroute, name='questroute'),
    path('questmenu', views.questmenu, name='questmenu'),
    path('getquests', views.getquests, name='getquests')
]
