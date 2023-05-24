from django.db import models
from django.contrib.auth.models import User

class DjangoContentType(models.Model):
    id = models.AutoField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = "django_content_type"

    def __str__(self):
        return f"App: {self.app_label}\nModel: {self.model}"


class DjangoAdminLog(models.Model):
    id = models.AutoField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField()
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, on_delete=models.CASCADE, db_column='content_type_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')

    class Meta:
        db_table = "django_admin_log"

    def __str__(self):
        return f"Action Time: {self.action_time}\nObject: {self.object_repr}\nAction Flag: {self.action_flag}"


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = "django_migrations"

    def __str__(self):
        return f"App: {self.app}\nMigration: {self.name}\nApplied: {self.applied}"
