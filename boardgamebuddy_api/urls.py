"""
URL configuration for boardgamebuddy_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from boardgamebuddy_api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    ### WE ARE PLANNING TO DO ALL BG RELATED CALLS DIRECTLY TO THE MIDDLEMAN
    ### LEAVING THIS HERE IN CASE THAT CHANGES
    # path('boardgames/', views.game_list),
    # path('boardgames/<int:id>', views.game_details),

    path('users', views.user_list),
    path('users/<int:id>', views.user_details),
    path('users/<int:id>/favorites', views.user_boardgames),
]
