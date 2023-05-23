from django.db import models


class CarBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "car_brands"

    def __str__(self):
        return f"Car Brand: {self.name}\n" f"ID: {self.id}"


class CarModel(models.Model):
    id = models.AutoField(primary_key=True)
    car_brand_id = models.IntegerField()
    name = models.CharField(max_length=30)
    year = models.IntegerField()
    battery_capacity = models.FloatField()

    class Meta:
        db_table = "car_models"

    def __str__(self):
        return (
            f"Car Model: {self.name}\n"
            f"ID: {self.id}\n"
            f"Car Brand ID: {self.car_brand_id}\n"
            f"Year: {self.year}\n"
            f"Battery Capacity: {self.battery_capacity}"
        )
