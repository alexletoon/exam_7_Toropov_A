from django.contrib import admin

from book_app.models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'email', 'created_at', 'changed_at', 'status']
    list_filer= ['id', 'name', 'email', 'created_at', 'changed_at', 'status']
    search_fields=['name', 'created_at']
    fields=['name', 'email', 'status']


admin.site.register(Record, RecordAdmin)

