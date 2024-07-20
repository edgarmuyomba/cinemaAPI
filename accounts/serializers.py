from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account 
        fields = ('username', 'password')

    def create(self, validated_data):
        new_account = Account(username=validated_data['username'])
        new_account.set_password(validated_data['password'])
        new_account.save()
        return new_account