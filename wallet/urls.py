from django.urls import path
from .views import register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet

urlpatterns =[ 
    path("register/",register_customer, name="registration"),
    path("wallet/",register_wallet, name="wallet_registration"),
    path("account/",register_account, name="account_registration"),
    path("transaction/",register_transaction, name="transaction_registration"),
    path("card/",register_card, name="card_registration"),
    path("thirdparty/",register_thirdparty, name="thirdparty_registration"),
    path("notification/",register_notification, name="notification_registration"),
    path("receipt/",register_receipt, name="receipt_registration"),
    path("loan/",register_loan, name="loan_registration"),
    path("reward/",register_reward, name="reward_registration"),

]

   

