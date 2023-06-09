from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    id_tag = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=6)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=8)
    state = models.CharField(max_length=40)

    class Meta:
        db_table = "users"

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"ID Tag: {self.id_tag}\n"
            f"Email: {self.email}\n"
            f"Name: {self.name}\n"
            f"Phone: {self.phone}\n"
            f"Gender: {self.gender}\n"
            f"Address Line 1: {self.address_line_1}\n"
            f"Address Line 2: {self.address_line_2}\n"
            f"City: {self.city}\n"
            f"Postcode: {self.postcode}\n"
            f"State: {self.state}"
        )


class TokenModel(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return (
            f"Token ID: {self.id}\n"
            f"User ID: {self.user.id}\n"
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
