from django.urls import path
from .import views

urlpatterns=[

    path('api/approval/<int:E_id>/<int:V_id>/',views.approval,name='approval'),
    path('api/approval/request/<int:E_id>/<int:V_id>/',views.showrequest,name='show_request'),

]