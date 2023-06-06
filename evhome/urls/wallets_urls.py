from django.urls import path
from ..views.wallets import *

urlpatterns = [
    path("wallet/", WalletListView.as_view(), name="wallet"),
    path("wallet_transaction_types/", WalletTransactionTypeListView.as_view(), name="wallet_transaction_types"),
]