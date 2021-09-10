from rest_framework import serializers
from .models import Account, Log, Event

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'role', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        account = Account(
            username=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
            role=self.validated_data['role'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Incorrect password.'})
        account.set_password(password)
        account.save()
        return account

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['user_email', 'event_name', 'role', 'hours', 'comments']
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'event_name', 
            'contact_name', 
            'contact_email', 
            'contact_number', 
            'event_summary', 
            'role_description',
            'max_hours',
            'date',
            'time',
            'location',
            'active',
            'upcoming',
            'link' ]