from django.shortcuts import render
from notifications.models import Notification
from .serializers import NotificationSerializer
from rest_framework import status ,generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from customuser.models import User

# Create your views here.

class NotificationReadAPI(generics.GenericAPIView):
    queryset =Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (AllowAny,)
    def get( self, request,format = None ):
        try:
            user = User.objects.get(id=request.user.id)
            serializer = NotificationSerializer(user.notifications.read(), many=True)
            # notifications = Notification.objects.filter(recipient=request.user)
            # serializer = NotificationSerializer(notifications, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class NotificationUnreadAPI(generics.GenericAPIView):
    '''
    Notification Unread API
    '''
    queryset =Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (AllowAny,)
    
    def get( self, request, format=None ):
        try:
            user = User.objects.get(id=request.user.id)
            serializer = NotificationSerializer(user.notifications.unread(), many=True)
            # notifications = Notification.objects.filter(recipient=request.user)
            # serializer = NotificationSerializer(notifications, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
