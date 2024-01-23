from django.contrib import admin
from django.urls import path
from bot import views, load_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
]
