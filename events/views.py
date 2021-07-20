# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.views import generic
from rest_framework.views import APIView
from .models import Events
from .serializers import EventSerializer,EventupdateSerializer, NotificationSerializer
from rest_framework import status ,generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import status
from rest_framework import generics
from customuser.models import User
from events.models import EventCategory
from notifications.signals import notify
from notifications.models import Notification


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def Event_display_all(request):
    all_events=Events.objects.all()
    serializer=EventSerializer(all_events,many=True)
    return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def Event_display_id(request,E_id):
    event=Events.objects.get(id=E_id)
    serializer=EventSerializer(event,many=False)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def Event_display_specific(request,username):
    user = User.objects.get(username=username)
    event = Events.objects.filter(user=user,completed=False)
    serializer=EventSerializer(event,many=True)
    return Response(serializer.data)

from notifications.signals import notify
@api_view(['POST'])
def registerEvent(request):
    data=request.data
    print(data)
    try:
        Event=Events.objects.create(
            user=User.objects.get(username=data['username']),
            category=EventCategory.objects.get(category=data['category']),
            name=data['name'],
            location=data['location'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            description=data['description'],
            completed=data['completed'],
        )
        serializer=EventSerializer(Event,many=False)
        Event=Events.objects.get(id=serializer.data['id'])
        Event.banner=request.FILES.get('banner')
        Event.save()
        serializer=EventSerializer(Event,many=False)
        notify.send(sender = request.user,recipient=User.objects.all().filter(volunteer = True),verb='has created an event',level=0)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        message={'detail':'Event with this content already exists'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

class EventUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventupdateSerializer

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def Event_display_completed(request,username):
    user = User.objects.get(username=username)
    event = Events.objects.filter(user=user,completed=True)
    serializer=EventSerializer(event,many=True)
    return Response(serializer.data)

class NotificationUnreadAPI(generics.GenericAPIView):
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




    


