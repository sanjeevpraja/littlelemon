from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [ 
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]


