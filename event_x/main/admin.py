from django.contrib import admin

from event_x.main.models import Event, MomentPhoto, Venue


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date_of_event')
    list_filter = ('date_of_event', 'location')
    search_fields = ('title',)


@admin.register(MomentPhoto)
class MomentPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'event', 'publication_date')
    list_filter = ('event', 'publication_date')
    search_fields = ('title',)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    list_filter = ('location',)
    search_fields = ('name',)

