"""
URL configuration for tir_lugansk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('shop/', include('shop.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Добавляем обслуживание статических файлов для продакшн
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Добавляем обслуживание изображений из папки images
if settings.DEBUG:
    urlpatterns += [
        path('images/<path:path>', serve, {
            'document_root': os.path.join(settings.BASE_DIR, 'images'),
        }),
    ]
else:
    # В продакшн режиме тоже добавляем раздачу изображений
    urlpatterns += [
        path('images/<path:path>', serve, {
            'document_root': os.path.join(settings.BASE_DIR, 'images'),
        }),
    ]
