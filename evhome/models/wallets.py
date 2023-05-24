from django.db import models
from django.contrib.auth.models import User
from .usergroups import UserGroupUser


class WalletTransactionType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "wallet_transaction_types"
        verbose_name = "Wallet Transaction Type"
        verbose_name_plural = "Wallet Transaction Types"

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class Wallet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="wallets", on_delete=models.CASCADE)
    balance = models.FloatField()
    user_group_user = models.ForeignKey(
        UserGroupUser, related_name="wallets", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "wallets"
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"

    def __str__(self):
        return f"ID: {self.id}, User ID: {self.user.id}, Balance: {self.balance}, User Group User ID: {self.user_group_user.id}"
