from django.db import models


class TokenModel(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        abstract = True

    def __str__(self):
        return (
            f"Token ID: {self.id}\n"
            f"User ID: {self.user_id}\n"
            f"Created at: {self.created_at}"
        )


class AdminAuthTokens(TokenModel):
    class Meta:
        db_table = "admin_auth_tokens"
        verbose_name_plural = "admin auth tokens"

    def __str__(self):
        return f"Admin Auth Token\n{super().__str__()}"


class AuthTokens(TokenModel):
    class Meta:
        db_table = "auth_tokens"
        verbose_name_plural = "auth tokens"

    def __str__(self):
        return f"Auth Token\n{super().__str__()}"
