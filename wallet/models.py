from django.db import models
from e_wallet.utils.choices import WalletCurrencySymbol

from e_wallet.utils.models import NamedTimeBasedModel, TimeBasedModel
from django_project.settings.base import AUTH_USER_MODEL


class Wallet(TimeBasedModel):
    owner = models.OneToOneField(AUTH_USER_MODEL, verbose_name="Owner", on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(verbose_name="Balance")
    currency = models.ForeignKey(
        "wallet.WalletCurrency", verbose_name="Currency", related_name="currency", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"

    def __str__(self) -> str:
        return self.owner.email

    @property
    def balance_and_symbol(self):
        return f"<span>{self.currency.symbol}</span> {self.balance}"


class WalletCurrency(NamedTimeBasedModel):
    code = models.CharField(verbose_name="Code", max_length=10)
    symbol = models.CharField(
        verbose_name="Symbol", max_length=10, choices=WalletCurrencySymbol.choices, default="&#8358"
    )

    class Meta:
        verbose_name = "Wallet Currency"
        verbose_name_plural = "Wallet Currencies"

    def __str__(self) -> str:
        return self.code
