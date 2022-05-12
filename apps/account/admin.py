from django.contrib import admin

from apps.account.models.accounts.account import Account,AccountUser


admin.site.register(Account)
admin.site.register(AccountUser)


