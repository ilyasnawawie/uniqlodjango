from django.db import models


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
        db_table = "ev_auth_user"

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Username: {self.username}\n"
            f"Email: {self.email}\n"
            f"Is Active: {self.is_active}\n"
            f"Date Joined: {self.date_joined}"
        )
