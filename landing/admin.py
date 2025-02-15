from django.contrib import admin
from .models import AccessLog

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user_agent', 'referer', 'accessed_at')
    search_fields = ('ip_address', 'user_agent', 'referer')
    list_filter = ('accessed_at',)