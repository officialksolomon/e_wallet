from django.db import models
from e_wallet.utils.models import NamedTimeBasedModel, TimeBasedModel
# Create your models here.

class Transaction(TimeBasedModel):
    reference = models.CharField(verbose_name="Reference" max_length=50)
    type = models.ForeignKey("transactions.TransactionTypr", verbose_name="Type", on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name="Amount")
    
    
class TransactionType(NamedTimeBasedModel):
    charge = models.PositiveIntegerField()
    
    
    
