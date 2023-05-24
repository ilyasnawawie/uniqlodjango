from django.db import models
from django.contrib.auth.models import User
from .chargelocation import ChargePoints, ChargePointLocations
from .chargepointport import ChargePointPort


class FaultTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "fault_types"
        verbose_name = "Fault Type"
        verbose_name_plural = "Fault Types"

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class Faults(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    fault_type = models.ForeignKey(
        FaultTypes, on_delete=models.CASCADE, db_column="fault_type_id"
    )
    charge_point_location = models.ForeignKey(
        ChargePointLocations,
        on_delete=models.CASCADE,
        db_column="charge_point_location_id",
    )
    charge_point = models.ForeignKey(
        ChargePoints, on_delete=models.CASCADE, db_column="charge_point_id"
    )
    charge_point_port = models.ForeignKey(
        ChargePointPort, on_delete=models.CASCADE, db_column="charge_point_port_id"
    )
    timestamp = models.DateTimeField()
    description = models.CharField(max_length=500)

    class Meta:
        db_table = "faults"
        verbose_name = "Fault"
        verbose_name_plural = "Faults"

    def __str__(self):
        return f"ID: {self.id}, User ID: {self.user.id}, Fault Type ID: {self.fault_type.id}, Charge Point Location ID: {self.charge_point_location.id}, Charge Point ID: {self.charge_point.id}, Charge Point Port ID: {self.charge_point_port.id}, Timestamp: {self.timestamp}, Description: {self.description}"
