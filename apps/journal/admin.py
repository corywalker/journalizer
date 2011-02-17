from django.contrib import admin
from journal.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('get_preview', 'date_added',)
    list_filter = ('date_added',)
    search_fields = ['text',]

admin.site.register(Entry, EntryAdmin)
