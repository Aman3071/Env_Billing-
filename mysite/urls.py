from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from invoices import views
from accounts import views as account_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Home
    path("", views.home, name="home"),
    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    # Customer
    path("customer/", views.customer, name="customer"),
    # Invoices
    path("invoices/", views.invoices, name="invoices"),
    # Add Invoice
    path("invoice-add/", views.add_invoice, name="add_invoice"),
    # Edit Invoice
    path("invoice-edit/<int:id>/", views.edit_invoice, name="edit_invoice"),
    # Delete Invoice
    path("invoice-delete/<int:id>/", views.delete_invoice, name="delete_invoice"),
    # Contact
    path("contact/", views.contact, name="contact"),
    # About
    path("about/", views.about, name="about"),
    # ORM - Create
    path("create-invoice/", views.create_invoice, name="create_invoice"),
    # ORM - Read One
    path("show-invoice/", views.show_one_invoice, name="show_one_invoice"),
    # ORM - Filter
    path("unpaid-invoices/", views.show_unpaid_invoices, name="show_unpaid_invoices"),
    # ORM - Update
    path("mark-paid/", views.mark_as_paid, name="mark_as_paid"),
    # Login and Logout
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("Logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", account_views.signup, name="signup"),
]
