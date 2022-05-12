from requests import Response

#modules
from apps.account.models.accounts.account import Account,AccountUser

#serializers
from apps.authentication.serializers.account.serializer import AccountSerializer,AccountUserSerializer

from rest_framework import viewsets,permissions

#viewsets
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountUserViewSet(viewsets.ModelViewSet):
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer
    permission_classes = [permissions.IsAuthenticated]

