from django.db import models
from django.contrib.auth.models import User
from .chargepointport import ChargePointPort

class OrderTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'order_types'

class OrderStatusTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'order_status_types'

class OrderStatusReasonTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

    class Meta:
        db_table = 'order_status_reason_types'

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
