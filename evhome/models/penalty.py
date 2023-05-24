from django.db import models
from django.contrib.auth.models import User
from .chargepointport import ChargePointPort
from .orders import Orders


class PenaltyStatusTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "penalty_status_types"

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class Penalties(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, db_column="order_id")
    penalty_no = models.CharField(max_length=15)
    timestamp = models.DateTimeField()

    class Meta:
        db_table = "penalties"

    def __str__(self):
        return f"ID: {self.id}, Type: {self.type}, User ID: {self.user.id}, Order ID: {self.order.id}, Penalty No: {self.penalty_no}, Timestamp: {self.timestamp}"


class PenaltyCharges(models.Model):
    id = models.AutoField(primary_key=True)
    charge_point_port = models.ForeignKey(
        ChargePointPort, on_delete=models.CASCADE, db_column="charge_point_port_id"
    )
    start_time = models.IntegerField()
    price = models.FloatField()

    class Meta:
        db_table = "penalty_charges"

    def __str__(self):
        return f"ID: {self.id}, Charge Point Port ID: {self.charge_point_port.id}, Start Time: {self.start_time}, Price: {self.price}"


class PenaltyStatus(models.Model):
    id = models.AutoField(primary_key=True)
    penalty = models.ForeignKey(
        Penalties, on_delete=models.CASCADE, db_column="penalty_id"
    )
    penalty_status_type = models.ForeignKey(
        PenaltyStatusTypes, on_delete=models.CASCADE, db_column="penalty_status_type_id"
    )
    timestamp = models.DateTimeField()
    amount = models.FloatField()

    class Meta:
        db_table = "penalty_status"

    def __str__(self):
        return f"ID: {self.id}, Penalty ID: {self.penalty.id}, Penalty Status Type ID: {self.penalty_status_type.id}, Timestamp: {self.timestamp}, Amount: {self.amount}"
