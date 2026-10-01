# Register your models here.
from django.contrib import admin
from .models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        "invoice_number",
        "customer_name",
        "amount",
        "invoice_date",
        "is_paid",
    ]
    search_fields = ["invoice_number", "customer_name"]
    list_filter = ["is_paid", "invoice_date"]
    ordering = ["-invoice_date"]


admin.site.register(Invoice, InvoiceAdmin)
