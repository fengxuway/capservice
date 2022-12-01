from django.contrib import admin

from .models import CapData


class CapDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_path')


admin.site.register(CapData, CapDataAdmin)
