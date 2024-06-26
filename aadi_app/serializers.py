from rest_framework import serializers
from .models import User, AuthToken, PasswordResetToken, UserActivity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'bio', 'first_name', 'last_name', 'email','is_superuser','is_staff','is_active']
       
class AuthTokenSerializer(serializers.ModelSerializer):

    user = UserSerializer(source = 'user')
    class Meta:
        model = AuthToken
        fields = ['id', 'user', 'token', 'created_at', 'updated_at']


class PasswordResetTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordResetToken
        fields = '__all__'


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'

