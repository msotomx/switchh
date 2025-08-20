from django.contrib import admin
from leads.models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("creado", "nombre", "email", "telefono", "empresa")
    search_fields = ("nombre", "email", "empresa", "mensaje")
    date_hierarchy = "creado"
