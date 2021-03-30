from django.contrib import admin
from .models import Doctor, Contact_Info
from django.utils.safestring import mark_safe


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.pic.url}">')

@admin.register(Contact_Info)
class AdminForm(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
