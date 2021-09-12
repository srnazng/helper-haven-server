from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Log, Event, Volunteer

class AccountAdmin(UserAdmin):
	list_display = ('id', 'email','username', 'role', 'is_admin','is_staff')
	search_fields = ('email','username', 'first_name', 'last_name')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class VolunteerAdmin(admin.ModelAdmin):
	list_display = ('email', 'first_name', 'last_name', 'gender', 'dob', 'address', 'city', 'state', 'zip', 'skills', 'link')
	search_fields = ('first_name', 'last_name', 'email', 'address', 'city', 'state', 'zip', 'skills')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class LogAdmin(admin.ModelAdmin):
	list_display = ('id', 'user_email', 'event_name', 'role', 'hours', 'comments')
	search_fields = ('user_email', 'event_name', 'role', 'hours', 'comments')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class EventAdmin(admin.ModelAdmin):
	list_display = ('id',
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
			'link',
			'active',
			'upcoming')
	search_fields = ('event_name', 'contact_name', 'event_summary', 'role_description')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Volunteer, VolunteerAdmin)

