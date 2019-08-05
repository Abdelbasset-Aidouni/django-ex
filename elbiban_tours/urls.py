"""elbiban_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import index,voyage_page,services_page,about_page


urlpatterns = [
	path('', index,name='home'),
    path('voyages/',voyage_page,name='voyages'),
	path('demand/', include('demand_handler.urls'),name='demand'),
    path('services/',services_page,name='services'),
    path('about/',about_page,name='about'),
    path('admin/', admin.site.urls),
    path('administration/',include('administration.urls'),name='administration'),
    path('tracking/', include('tracking.urls')),
]





urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
