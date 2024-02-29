"""
URL configuration for CRM project.

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
from django.urls import path, include

from CRM import views
from django.contrib.auth.decorators import login_required, permission_required
from CRM.views import login_view, logout_view
from staffapp.views import ListStaffView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('clientapp.urls')),
    path('', include('inventoryapp.urls')),
    path('', include('serviceapp.urls')),
    path('', include('staffapp.urls')),
    path('', include('recordapp.urls')),
    path('', login_required(ListStaffView.as_view())),
    path('login/', login_view, name='loginSite'),
    path('logout/', logout_view, name='logoutSite'),
    path('api/', include('ClientListAPI.urls')),
    path('register/', views.register, name='register'),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
