from django.dispatch import receiver
from django.db.models.signals import post_save
from django_project.settings.base import AUTH_USER_MODEL
from wallet.models import Wallet, WalletCurrency


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_wallet(sender, instance, created, **kwargs):
    currency = WalletCurrency.objects.get(code="NGN")
    if created:
        Wallet.objects.create(owner=instance, balance=0, currency=currency)
