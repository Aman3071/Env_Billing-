from django import forms

from .models import Invoice


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice

        fields = [
            "customer_name",
            "customer_email",
            "customer_phone",
            "invoice_number",
            "due_date",
            "amount",
            "tax_amount",
            "discount",
            "total_amount",
            "is_paid",
            "payment_date",
            "payment_method",
            "description",
        ]

    def clean_amount(self):

        amount = self.cleaned_data.get("amount")

        if amount is not None and amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero!")

        return amount
