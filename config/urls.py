"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path

from editor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.home, name="home"),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('save/', views.save, name='save'),
    path('toggle-complete/', views.toggle_complete, name='toggle-complete'),
    path('review-complete/<int:pk>/',
         views.review_complete, name='review-complete'),
    path('new/', views.new, name='new'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('export/<int:pk>/', views.ny_times_pdf, name='ny_times_pdf'),
    path('test/<int:pk>/', views.test_pdf, name='ny_times_pdf'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
