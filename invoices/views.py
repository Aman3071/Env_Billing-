from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Invoice
from .forms import InvoiceForm
from django.contrib.auth.decorators import login_required

# ================================
# Add Invoice
# ================================


def add_invoice(request):

    if request.method == "POST":

        form = InvoiceForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("invoices")

    else:

        form = InvoiceForm()

    return render(request, "add_invoice.html", {"form": form})


# ================================
# Edit Invoice
# ================================


def edit_invoice(request, id):

    invoice = get_object_or_404(Invoice, id=id)

    if request.method == "POST":

        form = InvoiceForm(request.POST, instance=invoice)

        if form.is_valid():

            form.save()

            return redirect("invoices")

    else:

        form = InvoiceForm(instance=invoice)

    return render(request, "edit_invoice.html", {"form": form})


# ================================
# Delete Invoice
# ================================


def delete_invoice(request, id):

    invoice = get_object_or_404(Invoice, id=id)

    if request.method == "POST":

        invoice.delete()

        return redirect("invoices")

    return render(request, "delete_invoice.html", {"invoice": invoice})


# ================================
# Invoice List
# ================================


@login_required(login_url="login")
def invoices(request):

    invoices = Invoice.objects.all()

    data = {"invoices": invoices}

    return render(request, "invoices.html", data)


# ================================
# ORM - Create Invoice
# ================================


def create_invoice(request):

    Invoice.objects.create(
        customer_name="Pankaj Tripathi",
        customer_email="pankaj.tripathi@example.com",
        customer_phone="9876543210",
        invoice_number="INV-001",
        due_date="2026-10-05",
        amount=25000.00,
        tax_amount=4500.00,
        discount=1000.00,
        total_amount=28500.00,
        is_paid=False,
        payment_method="UPI",
        description="Web application development and maintenance services.",
    )

    return render(request, "invoices.html", {})


# ================================
# ORM - Read One Invoice
# ================================


def show_one_invoice(request):

    invoice = Invoice.objects.get(invoice_number="INV-001")

    data = {"invoices": [invoice]}

    return render(request, "customer_name.html", data)


# ================================
# ORM - Filter
# ================================


def show_unpaid_invoices(request):

    invoices = Invoice.objects.filter(is_paid=False)

    data = {"invoices": invoices}

    return render(request, "customer_name.html", data)


# ================================
# ORM - Update
# ================================


def mark_as_paid(request):

    Invoice.objects.filter(invoice_number="INV-001").update(is_paid=True)

    invoices = Invoice.objects.filter(is_paid=False)

    data = {"invoices": invoices}

    return render(request, "customer_name.html", data)


# ================================
# Customer
# ================================


@login_required(login_url="login")
def customer(request):

    invoices = Invoice.objects.all()

    data = {"invoices": invoices}

    return render(request, "customer_name.html", data)


# ================================
# Home
# ================================


def home(request):

    return render(request, "home.html")


# ================================
# Dashboard
# Login Required
# ================================


@login_required(login_url="login")
def dashboard(request):

    total_invoices = Invoice.objects.count()

    paid_invoices = Invoice.objects.filter(is_paid=True).count()

    pending_invoices = Invoice.objects.filter(is_paid=False).count()

    total_amount = sum(invoice.total_amount for invoice in Invoice.objects.all())

    data = {
        "total_invoices": total_invoices,
        "paid_invoices": paid_invoices,
        "pending_invoices": pending_invoices,
        "total_amount": total_amount,
    }

    return render(request, "dashboard.html", data)


# ================================
# Contact
# ================================


def contact(request):

    return render(request, "contact.html")


# ================================
# About
# ================================


def about(request):

    return render(request, "about.html")
