from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""

    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(style={'input_type':'password'}, min_length=8, write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name", "username", "email", "password", "phone",)


    def validate_username(self, username):
        if self.context.get("is_create"):
        # if self.context['request'].method=="POST":
            if username:
                if CustomUser.objects.filter(username=username).exists():
                    raise ValidationError("Username already exists!!")
        return username

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user without setting a password correctly and return it"""
        password = validated_data.pop('password', None)

        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user