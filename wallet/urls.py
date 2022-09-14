from django.urls import path
from .views import list_account, list_card, list_customer, list_loan, list_notification, list_receipt, list_reward, list_thirdparty, list_transaction, list_wallet, register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet

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
    path("customers/",list_customer, name="customer_list"),
    path("wallets/",list_wallet, name="wallet_list"),
    path("accounts/",list_account,name ="account_list"),
    path("transactions/", list_transaction,name="transaction_list"),
    path("cards/",list_card,name="card_list"),
    path("thirdparties/",list_thirdparty, name="thirdparty_list"),
    path("notifications/",list_notification, name="notification_list"),
    path("receipts/",list_receipt,name="receipt_list"),
    path("loans/",list_loan,name="loan_list"),
    path("rewards/",list_reward,name="reward_list")



]

   

