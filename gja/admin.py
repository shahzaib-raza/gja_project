from django.contrib import admin
from .models import Member, Event

admin.site.site_header = "GJA Administration"
admin.site.site_title = "GJA Admin Portal"
admin.site.index_title = "Welcome to GJA Management"

# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    ordering = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start_date', 'end_date', 'created_at')
    list_filter = ('location', 'start_date', 'end_date')
    search_fields = ('title', 'short_description', 'description', 'location')
    ordering = ('-start_date',)
    date_hierarchy = 'start_date'

    # Optional: auto-fill slug from title
    prepopulated_fields = {'slug': ('title',)}