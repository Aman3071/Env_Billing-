from django.db import models

# Create your models here.

# 1 Invoice


class Invoice(models.Model):

    # Customer Details
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)

    # Invoice Details
    invoice_number = models.CharField(max_length=20, unique=True)

    invoice_date = models.DateField(auto_now_add=True)

    due_date = models.DateField()

    # Amount Details
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Payment Details
    is_paid = models.BooleanField(default=False)

    payment_date = models.DateField(null=True, blank=True)

    payment_method = models.CharField(
        max_length=50,
        choices=[
            ("Cash", "Cash"),
            ("UPI", "UPI"),
            ("Card", "Card"),
            ("Bank Transfer", "Bank Transfer"),
        ],
        blank=True,
    )

    # Additional Information
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice_number
