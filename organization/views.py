from volunteer.models import requestevents
from .serializer import RequestFormSerializer, approvalSerializer,requestedSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from customuser.models import User
from events.models import Events
from .models import requestform
from notifications.signals import notify

from notifications.signals import notify #notifications 
# Create your views here.
@api_view(['POST'])
def showrequest(request,E_id,V_id):
    try:
        approval=requestevents.objects.filter(user_id=V_id ,event_id=E_id)
        serializer=approvalSerializer(approval,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except requestevents.DoesNotExist:
         return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def approval(request,E_id,V_id):
    try:
        approval=requestevents.objects.get(user_id=V_id ,event_id=E_id)
        serializer=approvalSerializer(approval,data=request.data, partial  =True)
        if serializer.is_valid(): 
            serializer.save()
            if serializer.data['approved'] == True:
                notify.send(sender = request.user, recipient = User.objects.get(id = serializer.data['user']), verb = 'approved your request for')
            else:
                notify.send(sender = request.user, recipient = User.objects.get(id  = serializer.data['user']), verb = 'rejected your request for')
            return Response (serializer.data, status  = status.HTTP_200_OK)
        else:
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except requestevents.DoesNotExist:
            return Response ({"Exeption":"Does not exists"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def show_all_requested(request,E_id):
    try:
        requested=requestevents.objects.filter(event_id=E_id,request_volunteer=True)
        serializer=requestedSerializer(requested,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except requestevents.DoesNotExist:
         return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def requestforms(request):
    data=request.data
    try:
        form=requestform.objects.create(
            event=Events.objects.get(name=data['name']),
            ques_1=data['ques_1'],
            ques_2=data['ques_2'],
            ques_3=data['ques_3'],
        )
        serializer=RequestFormSerializer(form,many=False)
        return Response(serializer.data)
    except:
        message={'detail':'you have already updated the form'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getrequestedform(request,E_id):
    try:
        requestedform=requestform.objects.get(event_id=E_id)
        serializer=RequestFormSerializer(requestedform,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except requestevents.DoesNotExist:
         return Response(status=status.HTTP_400_BAD_REQUEST)
