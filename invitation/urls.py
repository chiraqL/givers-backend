from django.urls import path
from .import views


urlpatterns = [

    path('api/invite/<int:U_id>/<int:E_id>/', views.invite, name='invite'),
    path('api/invite/<int:U_id>/', views.invite_display_id, name='invitation'),
    path('api/invite/read/<int:I_id>/',
         views.invite_display_id_read, name='invitation_read'),



]
