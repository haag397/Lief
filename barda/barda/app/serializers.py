from rest_framework import serializers
from .models import AdminData, UserData, Rules


class AdminDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminData
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "rule_id",
        ]
        read_only_fields = ["id", "date_joined", "last_edit"]


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["id", "username", "password", "email", "first_name", "last_name"]
        read_only_fields = ["id", "date_joined", "last_edit", "created_by_id"]


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = "__all__"
