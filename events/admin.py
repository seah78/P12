from django.contrib import admin


from events.models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 
                    'status', 'contract', 
                    'support_user')
    list_filter = ('contract',)
    search_fields = ('name', 'status', 'contract')

