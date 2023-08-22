from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["email"]
    exclude = ["password"]

    fieldsets = [
        ["Main", {
            "fields": ["first_name", "last_name", "email", "username", "is_active"]
        }],
        ["Systemic", {
            "fields": ["last_login", "date_joined", "is_superuser", "is_staff"]
        }],
        ["Permissions", {
            "fields": ["groups", "user_permissions"]
        }],
        ["Stripe", {
            "fields": [
                "stripe_subscription_id", 
                "stripe_customer_id"
            ]
        }]
    ]