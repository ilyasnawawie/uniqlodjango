from django.db import models
from django.contrib.auth.models import User
from .chargepointport import ChargePointPort

class OrderTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'order_types'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class OrderStatusTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'order_status_types'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class OrderStatusReasonTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

    class Meta:
        db_table = 'order_status_reason_types'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    charge_point_port = models.ForeignKey(ChargePointPort, on_delete=models.CASCADE, db_column='charge_point_port_id')
    order_no = models.CharField(max_length=15)
    order_type = models.ForeignKey(OrderTypes, on_delete=models.CASCADE, db_column='order_type_id')
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"ID: {self.id}, Type: {self.type}, User ID: {self.user.id}, Charge Point Port ID: {self.charge_point_port.id}, Order No: {self.order_no}, Order Type ID: {self.order_type.id}, Timestamp: {self.timestamp}"


class OrderStatus(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, db_column='order_id')
    order_status_type = models.ForeignKey(OrderStatusTypes, on_delete=models.CASCADE, db_column='order_status_type_id')
    timestamp = models.DateTimeField()
    meter_value = models.FloatField()
    amount = models.FloatField()
    reason_type = models.ForeignKey(OrderStatusReasonTypes, on_delete=models.CASCADE, db_column='reason_type_id')

    class Meta:
        db_table = 'order_status'

    def __str__(self):
        return f"ID: {self.id}, Order ID: {self.order.id}, Order Status Type ID: {self.order_status_type.id}, Timestamp: {self.timestamp}, Meter Value: {self.meter_value}, Amount: {self.amount}, Reason Type ID: {self.reason_type.id}"