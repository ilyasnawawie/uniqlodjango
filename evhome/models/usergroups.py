from django.db import models
from django.contrib.auth.models import User


class UserGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = "user_groups"
        verbose_name = "User Group"
        verbose_name_plural = "User Groups"

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class UserGroupUser(models.Model):
    id = models.AutoField(primary_key=True)
    user_group = models.ForeignKey(
        UserGroup, related_name="users", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, related_name="user_groups", on_delete=models.CASCADE)
    is_operator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = "user_group_users"
        verbose_name = "User Group User"
        verbose_name_plural = "User Group Users"

    def __str__(self):
        return f"ID: {self.id}, User Group ID: {self.user_group.id}, User ID: {self.user.id}, Is Operator: {self.is_operator}, Is Admin: {self.is_admin}"


class UserGroupUserRfidStatusType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "user_group_user_rfid_status_types"
        verbose_name = "User Group User RFID Status Type"
        verbose_name_plural = "User Group User RFID Status Types"

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class UserGroupUserRfid(models.Model):
    id = models.AutoField(primary_key=True)
    user_group_user = models.ForeignKey(
        UserGroupUser, related_name="rfids", on_delete=models.CASCADE
    )
    rfid = models.CharField(max_length=20)
    status_type = models.ForeignKey(
        UserGroupUserRfidStatusType, on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_group_user_rfids"
        verbose_name = "User Group User RFID"
        verbose_name_plural = "User Group User RFIDs"

    def __str__(self):
        return f"ID: {self.id}, User Group User ID: {self.user_group_user.id}, RFID: {self.rfid}, Status Type ID: {self.status_type.id}, Timestamp: {self.timestamp}"
