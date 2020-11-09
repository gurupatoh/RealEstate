from django.contrib import admin
from .models import Realtors


class RealtorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'date_hired')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Realtors, RealtorsAdmin)
