from django.db import models

class AdminAuthTokens(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'admin_auth_tokens'

    def __str__(self):
        return f"Token ID: {self.id}, User ID: {self.user_id}, Created at: {self.created_at}"
    
class AuthTokens(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'auth_tokens'

    def __str__(self):
        return f"Token ID: {self.id}, User ID: {self.user_id}, Created at: {self.created_at}"