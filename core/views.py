# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view
from .serializers import RegistrationSerializer, LogSerializer, EventSerializer
from .models import Account, Log, Event
from rest_framework.authtoken.models import Token
from django.db.models import F, Sum

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered new user."
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['username'] = account.username
            data['role'] = account.role
            data['email'] = account.email
            data['token'] = Token.objects.get(user=account).key
            return Response(data)
        return Response(serializer.errors)

class ProfileView(APIView):
    @api_view(('GET', 'PATCH'))
    def profile(request, user_email):
        qs = Account.objects.filter(email = user_email)
        data = {}
        if len(qs) > 0:
            account = qs[0]
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['role'] = account.role
            data['email'] = account.email
            return Response(data)
        else:
            data['response'] = "Failed to fetch user profile."
            return Response(data)

    def patch(self, request, user_email):
        account = Account.objects.get(username=user_email)
        serializer = RegistrationSerializer(account, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.update(account, request.data)
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['role'] = account.role
            data['email'] = user_email
            return Response(data)
        data['response'] = "Wrong parameters."
        return Response(data)


class LogView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LogSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            log_event = serializer.save()
            data['response'] = "Successfully added new log entry."
            data['user_email'] = log_event.user_email
            data['event_name'] = log_event.event_name
            data['role'] = log_event.role
            data['hours'] = log_event.hours
            data['comments'] = log_event.comments
            return Response(data)
        return Response(serializer.errors)

    @api_view(('GET',))
    def getAll(request):
        qs = Log.objects.all()
        serializer = LogSerializer(qs, many=True)
        
        return Response(serializer.data)

    @api_view(('GET',))
    def getByUserEmail(request, user_email):
        qs = Log.objects.filter(user_email = user_email)

        serializer = LogSerializer(qs, many=True)
        return Response(serializer.data)

class EventView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        data = {}
    
        if serializer.is_valid():
            event = serializer.save()
            data['response'] = "Successfully added new event."
            data['id'] = event.id
            data['event_name'] = event.event_name
            data['contact_name'] = event.contact_name
            data['contact_email'] = event.contact_email
            data['contact_number'] = event.contact_number
            data['event_summary'] = event.event_summary
            data['role_description'] = event.role_description
            data['max_hours'] = event.max_hours
            data['date'] = event.date
            data['time'] = event.time
            data['location'] = event.location
            data['active'] = event.active
            data['upcoming'] = event.upcoming
            data['link'] = event.link
            return Response(data)
        return Response(serializer.errors)

    def get(self, request, *args, **kwargs):
        qs = Event.objects.all()
        serializer = EventSerializer(qs, many=True)
        return Response(serializer.data)