from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = validated_data.get('user')

        if user and user.is_superuser and validated_data.get['is_superuser']:
           user_created = User.objects.create_superuser(**validated_data)
        else:
            user_created = User.objects.create_user(**validated_data)
        # self.send_mail(user_created.email, user_created.username)
        return user_created
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_superuser', 'is_staff')