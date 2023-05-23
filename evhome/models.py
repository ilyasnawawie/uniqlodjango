from django.db import models

# Token Models

class TokenModel(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        abstract = True


class AdminAuthTokens(TokenModel):
    class Meta:
        db_table = 'admin_auth_tokens'

    def __str__(self):
        return f"Token ID: {self.id}, User ID: {self.user_id}, Created at: {self.created_at}"

class AuthTokens(TokenModel):
    class Meta:
        db_table = 'auth_tokens'

    def __str__(self):
        return f"Token ID: {self.id}, User ID: {self.user_id}, Created at: {self.created_at}"
    
# Auth Group Models

class AuthGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'ev_auth_group'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"
    
class AuthGroupPermisson(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        db_table = 'auth_group_permission'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

# Auth User 

class AuthUser(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'ev_auth_user'

    def __str__(self):
        return f"ID: {self.id}, Password: {self.password}, Last Login: {self.last_login}, Is Superuser: {self.is_superuser}, Username: {self.username}, First Name: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}, Is Staff: {self.is_staff}, Is Active: {self.is_active}, Date Joined: {self.date_joined}"


# Charge Point Locations    

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
        return f"Location ID: {self.id}, Name: {self.name}, Address: {self.address}"


