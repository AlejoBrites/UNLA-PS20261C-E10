from django.contrib import admin
from .models import LibraryEntry


@admin.register(LibraryEntry)
class LibraryEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'status', 'acquired_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'game__title')
    readonly_fields = ('acquired_at',)
