from rest_framework import serializers
#modules
from apps.account.models.accounts.account import Account,AccountUser

#serializers
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = '__all__'
