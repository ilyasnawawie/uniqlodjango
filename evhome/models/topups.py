from django.db import models
from django.contrib.auth.models import User
from .usergroups import UserGroupUser

class TopUpType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

    class Meta:
        db_table = 'top_up_types'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class TopUp(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(TopUpType, related_name='top_ups', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='top_ups', on_delete=models.CASCADE)
    top_up_no = models.CharField(max_length=15)
    top_up_type = models.ForeignKey(TopUpType, on_delete=models.CASCADE)
    user_group_user = models.ForeignKey(UserGroupUser, related_name='top_ups', on_delete=models.CASCADE)
    operated_by = models.ForeignKey(User, related_name='operated_top_ups', on_delete=models.CASCADE)

    class Meta:
        db_table = 'top_ups'

    def __str__(self):
        return f"ID: {self.id}, Type ID: {self.type.id}, User ID: {self.user.id}, Top-Up No: {self.top_up_no}, Top-Up Type ID: {self.top_up_type.id}, User Group User ID: {self.user_group_user.id}, Operated by User ID: {self.operated_by.id}"

class TopUpStatusType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'top_up_status_types'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class TopUpStatus(models.Model):
    id = models.AutoField(primary_key=True)
    top_up = models.ForeignKey(TopUp, related_name='statuses', on_delete=models.CASCADE)
    top_up_status_type = models.ForeignKey(TopUpStatusType, related_name='statuses', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()

    class Meta:
        db_table = 'top_up_status'

    def __str__(self):
        return f"ID: {self.id}, Top-Up ID: {self.top_up.id}, Top-Up Status Type ID: {self.top_up_status_type.id}, Timestamp: {self.timestamp}, Amount: {self.amount}"
