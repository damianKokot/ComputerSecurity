from django.contrib import admin
from .models import Transaction, UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    readonly_fields = ["user"]
    list_display = ("user", "account_number", "balance")


class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ["pending"]
    list_display = ("from_account", "to_account", "amount",
                    "date", "message", "accepted")


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(UserAccount, UserAccountAdmin)
