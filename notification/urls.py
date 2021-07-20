from django.urls import path
from . import views

urlpatterns = [
    path('api/events/notifications/read/', views.NotificationUnreadAPI.as_view(),name='notifications_unread'),
    path('api/events/notifications/unread/', views.NotificationReadAPI.as_view(),name='notifications_read'),
]