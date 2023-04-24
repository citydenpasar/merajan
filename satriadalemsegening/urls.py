"""
URL configuration for satriadalemsegening project.

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
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="halaman_awal"),
    path('tambah_balasan/<int:komentar_id>/', views.index, name='tambah_balasan'),
    path('tambah-komentar/', views.tambah_komentar, name='tambah_komentar'),
    path('purnama/', views.purnama, name="purnama"),
    path('tilem/', views.tilem, name="tilem"),
    path('odalan/', views.odalan, name="odalan"),
    path('galungan/', views.galungan, name="galungan"),
    path('<int:betara_id>/',views.detailbetara, name='detailbetara'),
    path('edit-komentar/<int:komentar_id>/', views.edit_komentar, name='edit_komentar'),
    path('delete-komentar/<int:komentar_id>/', views.delete_komentar, name='delete_komentar'),
]
