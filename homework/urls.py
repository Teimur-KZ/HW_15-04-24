"""
URL configuration for homework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

# include - функция, которая позволяет включать другие URLconf
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homework_app.urls')),
    path('about/', include('homework_app.urls')),
]


handler404 = 'homework_app.views.error_404'
'''
Переключить в настройках DEBUG на True, чтобы увидеть страницу ошибки 404.
'''