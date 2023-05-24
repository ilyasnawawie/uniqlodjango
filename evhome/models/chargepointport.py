from django.db import models


class ChargePointPort(models.Model):
    id = models.AutoField(primary_key=True)
    charge_point_id = models.IntegerField()
    connector_id = models.IntegerField()
    name = models.CharField(max_length=100)
    electricity_type_id = models.IntegerField()
    type = models.CharField(max_length=45)
    power = models.FloatField()
    current = models.FloatField()
    voltage = models.FloatField()
    latest_status = models.IntegerField()
    latest_meter_value = models.FloatField()

    class Meta:
        db_table = "charge_point_ports"

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Charge Point ID: {self.charge_point_id}\n"
            f"Connector ID: {self.connector_id}\n"
            f"Name: {self.name}\n"
            f"Electricity Type ID: {self.electricity_type_id}\n"
            f"Type: {self.type}\n"
            f"Power: {self.power}\n"
            f"Current: {self.current}\n"
            f"Voltage: {self.voltage}\n"
            f"Latest Status: {self.latest_status}\n"
            f"Latest Meter Value: {self.latest_meter_value}"
        )


class ChargePointPortStatus(models.Model):
    charge_point_port = models.ForeignKey(ChargePointPort, on_delete=models.CASCADE)
    charge_point_port_status_type_id = models.IntegerField()
    charge_point_port_error_code_type_id = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        db_table = "charge_point_port_status"

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Charge Point Port ID: {self.charge_point_port_id}\n"
            f"Charge Point Port Status Type ID: {self.charge_point_port_status_type_id}\n"
            f"Charge Point Port Error Code Type ID: {self.charge_point_port_error_code_type_id}\n"
            f"Timestamp: {self.timestamp}"
        )


class ChargePointPortStatusTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=13)

    class Meta:
        db_table = "charge_point_port_status_types"

    def __str__(self):
        return f"ID: {self.id}\n" f"Name: {self.name}"


class ChargePointPortPrices(models.Model):
    charge_point_port = models.ForeignKey(ChargePointPort, on_delete=models.CASCADE)
    price = models.FloatField()

    class Meta:
        db_table = "charge_point_port_prices"

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Charge Point Port ID: {self.charge_point_port_id}\n"
            f"Price: {self.price}"
        )


class ChargePointPortMeterValues(models.Model):
    charge_point_port = models.ForeignKey(ChargePointPort, on_delete=models.CASCADE)
    energy_active_import_register = models.FloatField()
    power_active_import = models.FloatField()
    temperature = models.FloatField()
    voltage = models.FloatField()
    current_import = models.FloatField()

    class Meta:
        db_table = "charge_point_port_meter_values"

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Charge Point Port ID: {self.charge_point_port_id}\n"
            f"Energy Active Import Register: {self.energy_active_import_register}\n"
            f"Power Active Import: {self.power_active_import}\n"
            f"Temperature: {self.temperature}\n"
            f"Voltage: {self.voltage}\n"
            f"Current Import: {self.current_import}"
        )


class ChargePointPortErrorCodeTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "charge_point_port_error_code_types"

    def __str__(self):
        return f"ID: {self.id}\n" f"Name: {self.name}"
