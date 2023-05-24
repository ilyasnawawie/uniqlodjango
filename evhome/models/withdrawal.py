from django.db import models
from django.contrib.auth.models import User
from .usergroups import UserGroupUser


class WithdrawalStatusType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "withdrawal_status_types"
        verbose_name = "Withdrawal Status Type"
        verbose_name_plural = "Withdrawal Status Types"

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class WithdrawalType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "withdrawal_types"
        verbose_name = "Withdrawal Type"
        verbose_name_plural = "Withdrawal Types"

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class Withdrawal(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(
        WithdrawalType, related_name="withdrawals", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, related_name="withdrawals", on_delete=models.CASCADE)
    withdrawal_no = models.CharField(max_length=15)
    withdrawal_type = models.ForeignKey(WithdrawalType, on_delete=models.CASCADE)
    user_group_user = models.ForeignKey(
        UserGroupUser, related_name="withdrawals", on_delete=models.CASCADE
    )
    operated_by = models.ForeignKey(
        User, related_name="operated_withdrawals", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "withdrawals"
        verbose_name = "Withdrawal"
        verbose_name_plural = "Withdrawals"

    def __str__(self):
        return f"ID: {self.id}, Type ID: {self.type.id}, User ID: {self.user.id}, Withdrawal No: {self.withdrawal_no}, Withdrawal Type ID: {self.withdrawal_type.id}, User Group User ID: {self.user_group_user.id}, Operated by User ID: {self.operated_by.id}"


class WithdrawalStatus(models.Model):
    id = models.AutoField(primary_key=True)
    withdrawal = models.ForeignKey(
        Withdrawal, related_name="statuses", on_delete=models.CASCADE
    )
    withdrawal_status_type = models.ForeignKey(
        WithdrawalStatusType, related_name="statuses", on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()

    class Meta:
        db_table = db_table = "withdrawal_status"
        verbose_name = "Withdrawal Status"
        verbose_name_plural = "Withdrawal Statuses"

    def __str__(self):
        return f"ID: {self.id}, Withdrawal ID: {self.withdrawal.id}, Withdrawal Status Type ID: {self.withdrawal_status_type.id}, Timestamp: {self.timestamp}, Amount: {self.amount}"
