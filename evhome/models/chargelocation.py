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
