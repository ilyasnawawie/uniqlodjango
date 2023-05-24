from django.db import models
from django.contrib.auth.models import User
from .chargepointport import ChargePointPort
from .orders import Orders
from .chargepointport import ChargePointPort
from .orders import Orders


class ReservationStatusTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "reservation_status_types"

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class Reservations(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    charge_point_port = models.ForeignKey(
        ChargePointPort, on_delete=models.CASCADE, db_column="charge_point_port_id"
    )
    reservation_no = models.CharField(max_length=15)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        db_table = "reservations"

    def __str__(self):
        return f"ID: {self.id}, User ID: {self.user.id}, Charge Point Port ID: {self.charge_point_port.id}, Reservation No: {self.reservation_no}, Start Time: {self.start_time}, End Time: {self.end_time}"


class ReservationStatus(models.Model):
    id = models.AutoField(primary_key=True)
    reservation = models.ForeignKey(
        Reservations, on_delete=models.CASCADE, db_column="reservation_id"
    )
    reservation_status_type = models.ForeignKey(
        ReservationStatusTypes,
        on_delete=models.CASCADE,
        db_column="reservation_status_type_id",
    )
    timestamp = models.DateTimeField()

    class Meta:
        db_table = "reservation_status"

    def __str__(self):
        return f"ID: {self.id}, Reservation ID: {self.reservation.id}, Reservation Status Type ID: {self.reservation_status_type.id}, Timestamp: {self.timestamp}"


class ReservationOrderRelations(models.Model):
    id = models.AutoField(primary_key=True)
    reservation = models.ForeignKey(
        Reservations, on_delete=models.CASCADE, db_column="reservation_id"
    )
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, db_column="order_id")

    class Meta:
        db_table = "reservation_order_relations"

    def __str__(self):
        return f"ID: {self.id}, Reservation ID: {self.reservation.id}, Order ID: {self.order.id}"
