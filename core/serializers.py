from rest_framework import serializers
from .models import Account, Log, Event, Volunteer, Organization

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = Account
        fields = ['id', 'email', 'role', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        account = Account(
            username=self.validated_data['email'],
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
        fields = ['id', 'user_email', 'event_name', 'role', 'hours', 'comments']

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['email', 'first_name', 'last_name', 'gender', 'dob', 'address', 'city', 'state', 'zip', 'skills', 'link']

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['email', 'name', 'description', 'phone', 'address', 'city', 'state', 'zip', 'category', 'link']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'event_name', 
            'org_name',
            'org_email',
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
            'link',
            'skills' ]