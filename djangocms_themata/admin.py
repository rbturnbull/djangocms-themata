from django.contrib import admin

from .models import Stylesheet

@admin.register(Stylesheet)
class StylesheetAdmin(admin.ModelAdmin):
    list_filter = ['active', 'category',]
    list_display = ['__str__', 'active', 'category']
    list_editable = ['active',]
