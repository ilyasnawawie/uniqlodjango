from django.db import models


class AuthGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "ev_auth_group"

    def __str__(self):
        return f"ID: {self.id}\n" f"Name: {self.name}"


class AuthGroupPermission(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE, db_column="group_id")
    permission_id = models.IntegerField()

    class Meta:
        db_table = "auth_group_permission"

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Group ID: {self.group.id}\n"
            f"Permission ID: {self.permission_id}"
        )
