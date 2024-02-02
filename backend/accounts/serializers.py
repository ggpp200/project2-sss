from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "name",
            "email",
            "phone_number",
            "department",
        )
    def create(self,validated_data):
        password = validated_data.pop("password",None)
        instance = self.Meta.model(**validated_data)
        if password is not None :
        #provide django, password will be hashing!
            instance.set_password(password)
            instance.save()
            return instance

class UserActiveSeriailzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "activation",
        )

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "name",
            "email",
            "phone_number",
            "department",
            "is_admin"
        )

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "name",
            "email",
            "phone_number",
            "department",
            "activation",
        )