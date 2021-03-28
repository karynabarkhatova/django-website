from django.contrib import admin
from .models import Doctor
from django.utils.safestring import mark_safe


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.pic.url}">')
