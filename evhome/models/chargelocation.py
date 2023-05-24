from django.db import models


class ChargePointLocations(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    class Meta:
        db_table = "charge_point_locations"

    def __str__(self):
        return (
            f"Location ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Address: {self.address}"
        )


class ChargePointLocationOwnerships(models.Model):
    id = models.AutoField(primary_key=True)
    charge_point_location = models.ForeignKey(ChargePointLocations, on_delete=models.CASCADE, db_column='charge_point_location_id')
    # If you have a UserGroup model, you can also create a ForeignKey relationship here
    user_group_id = models.IntegerField()
    is_private = models.BooleanField()

    class Meta:
        db_table = "charge_point_location_ownerships"

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Charge Point Location ID: {self.charge_point_location.id}\n"
            f"User Group ID: {self.user_group_id}\n"
            f"Is Private: {self.is_private}"
        )

class ChargePoints(models.Model):
    id = models.AutoField(primary_key=True)
    charge_point_location = models.ForeignKey(ChargePointLocations, on_delete=models.CASCADE, db_column='charge_point_location_id')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    serial_number = models.CharField(max_length=25)
    model = models.CharField(max_length=20)
    vendor = models.CharField(max_length=20)
    firmware_version = models.CharField(max_length=50)
    iccid = models.CharField(max_length=20)
    imsi = models.CharField(max_length=20)
    meter_serial_number = models.CharField(max_length=25)
    meter_type = models.CharField(max_length=25)

    class Meta:
        db_table = "charge_points"

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Charge Point Location ID: {self.charge_point_location.id}\n"
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Serial Number: {self.serial_number}\n"
            f"Model: {self.model}\n"
            f"Vendor: {self.vendor}\n"
            f"Firmware Version: {self.firmware_version}\n"
            f"ICCID: {self.iccid}\n"
            f"IMSI: {self.imsi}\n"
            f"Meter Serial Number: {self.meter_serial_number}\n"
            f"Meter Type: {self.meter_type}"
        )
