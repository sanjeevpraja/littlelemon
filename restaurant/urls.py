from django.contrib import admin 
from django.urls import path, include
from . import views


urlpatterns = [ 
    #path('', views.sayHello, name='sayHello'), 
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
]


