from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.library, name='library'),
    path('update/<int:entry_id>/', views.update_status, name='update_status'),
]
