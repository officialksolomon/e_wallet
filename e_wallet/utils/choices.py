from django.db import models


class WalletCurrencySymbol(models.TextChoices):
    Naira = ("&#8358", "Naira")
