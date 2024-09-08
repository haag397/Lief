"""
create model for admin, user, rules
"""
from django.db import models
from nanoid import generate


def generate_nanoid():
    """use nanoID"""
    return generate(size=10)


class Rules(models.Model):
    """
    Represents a rule that can be assigned to an admin. Each admin should have one rule
    """

    id = models.CharField(
        primary_key=True,
        default=generate_nanoid,
        editable=False,
        max_length=21,
        unique=True,
    )
    rule_name = models.CharField(max_length=30, default="admin")
    description = models.TextField(
        max_length=40, default="can awrite but can not ddelet"
    )

    def __str__(self):
        return self.rule_name


class AdminData(models.Model):
    """
    Defines the attributes and behaviors of a admin
    """

    id = models.CharField(
        primary_key=True,
        default=generate_nanoid,
        editable=False,
        max_length=21,
        unique=True,
    )
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=40, unique=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True, blank=True)
    rule_name = models.ForeignKey(Rules, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["username", "password", "email", "lastname"]

    def __str__(self):
        return self.username


class UserData(models.Model):
    """
    Defines the attributes and behaviors of a user
    """

    id = models.CharField(
        primary_key=True,
        default=generate_nanoid,
        editable=False,
        max_length=21,
        unique=True,
    )
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=40, unique=True, null=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    created_by_id = models.ForeignKey(AdminData, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password", "username", "email", "lastname"]

    def __str__(self):
        return self.username
