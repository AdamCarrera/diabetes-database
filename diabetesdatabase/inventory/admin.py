from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Insulin, GlucoseMonitor, CareSupplies

@register(Insulin)
class InsulinAdmin(admin.ModelAdmin):
    list_display = ['brand', 'quantity', 'type']

@register(GlucoseMonitor)
class GlucoseMonitorAdmin(admin.ModelAdmin):
    list_display = ['type', 'quantity']

@register(CareSupplies)
class CareSuppliesAdmin(admin.ModelAdmin):
    list_display = ['type', 'quantity']