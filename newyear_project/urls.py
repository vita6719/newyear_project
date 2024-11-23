from django.contrib import admin
from django.urls import path
from holiday import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.holiday_view, name='holiday'),  # Главная страница
    path('holiday/', views.holiday_view, name='holiday_page'),  # Путь к странице с анимацией
]

