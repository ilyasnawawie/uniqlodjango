from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CarBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "car_brands"

    def __str__(self):
        return f"Car Brand: {self.name}\n" f"ID: {self.id}"


class CarModel(models.Model):
    id = models.AutoField(primary_key=True)
    car_brand = models.ForeignKey(
        CarBrand, on_delete=models.CASCADE, db_column="car_brand_id"
    )
    name = models.CharField(max_length=30)
    year = models.IntegerField()
    battery_capacity = models.FloatField()

    class Meta:
        db_table = "car_models"

    def __str__(self):
        return (
            f"Car Model: {self.name}\n"
            f"ID: {self.id}\n"
            f"Car Brand ID: {self.car_brand.id}\n"
            f"Year: {self.year}\n"
            f"Battery Capacity: {self.battery_capacity}"
        )


class UserCar(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="cars", on_delete=models.CASCADE)
    car_model = models.ForeignKey(
        CarModel, related_name="user_cars", on_delete=models.CASCADE
    )
    color = models.CharField(max_length=10)

    class Meta:
        db_table = "user_cars"

    def __str__(self):
        return (
            f"User ID: {self.user.id}\n"
            f"Car Model ID: {self.car_model.id}\n"
            f"Color: {self.color}"
        )
