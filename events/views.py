# Create your views here.

from .models import Events
from .serializers import EventSerializer, EventupdateSerializer
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from customuser.models import User
from category.models import EventCategory


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Event_display_all(request):
    all_events = Events.objects.all()
    serializer = EventSerializer(all_events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Event_display_id(request, E_id):
    event = Events.objects.get(id=E_id)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Event_display_specific(request, E_id):
    user = User.objects.get(id=E_id)
    event = Events.objects.filter(user=user, completed=False)
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Event_display_completed(request, E_id):
    user = User.objects.get(id=E_id)
    event = Events.objects.filter(user=user, completed=True)
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerEvent(request):
    data = request.data
    print(data)
    try:
        Event = Events.objects.create(
            user=User.objects.get(username=data['username']),
            category=EventCategory.objects.get(category=data['category']),
            name=data['name'],
            location=data['location'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            description=data['description'],
            completed=data['completed'],
        )
        serializer = EventSerializer(Event, many=False)
        Event = Events.objects.get(id=serializer.data['id'])
        Event.banner = request.FILES.get('banner')
        Event.save()
        serializer = EventSerializer(Event, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Event with this content already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class EventUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventupdateSerializer
