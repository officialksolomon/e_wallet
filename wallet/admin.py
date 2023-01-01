from django.contrib import admin

from wallet.models import Wallet, WalletCurrency

# Register your models here.


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ["owner", "balance", "currency"]
    list_filter = [
        "owner",
    ]
    ordering = ["owner"]
    search_fields = ["owner"]


@admin.register(WalletCurrency)
class WalletCurrencyAdmin(admin.ModelAdmin):
    list_display = ["name", "code"]
    list_filter = ["name"]
    ordering = ["created_at"]
    search_fields = ["name"]
