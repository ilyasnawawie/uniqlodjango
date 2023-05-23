from django.db import models

class ChargePointLocations(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    class Meta:
        db_table = 'charge_point_locations'

    def __str__(self):
        return f"Location ID: {self.id}\n" \
               f"Name: {self.name}\n" \
               f"Address: {self.address}"
