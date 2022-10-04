from unicodedata import name
from django.urls import path
from .views import account_profile, card_profile, customer_profile, edit_account, edit_profile, edit_receipt, edit_transaction, edit_wallet, list_account, list_card, list_customer, list_loan, list_notification, list_receipt, list_reward, list_thirdparty, list_transaction, list_wallet, register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet, transaction_profile, wallet_profile

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

    # listing data
    path("customers/",list_customer, name="customer_list"),
    path("wallets/",list_wallet, name="wallet_list"),
    path("accounts/",list_account,name ="account_list"),
    path("transactions/", list_transaction,name="transaction_list"),
    path("cards/",list_card,name="card_list"),
    path("thirdparties/",list_thirdparty, name="thirdparty_list"),
    path("notifications/",list_notification, name="notification_list"),
    path("receipts/",list_receipt,name="receipt_list"),
    path("loans/",list_loan,name="loan_list"),
    path("rewards/",list_reward,name="reward_list"),

    
    
    path("customers/<int:id>/", customer_profile,name="customer_profile"),
    path("customers/edit/<int:id>/", edit_profile,name="edit_profile"),

    # path("wallets/<int:id>/",wallet_profile,name="wallet_profile"),
    path("wallets/<int:id>/",wallet_profile,name="wallet_profile"),
    path("wallets/edit/<int:id>/",edit_wallet,name="edit_wallet"),

    path("accounts/<int:id>/",account_profile,name="account_profile"),
    path("accounts/edit/<int:id>/",edit_account,name="edit_account"),
    
    path("cards/<int:id>/",card_profile,name="card_profile"),
    path("cards/edit/<int:id>/",edit_profile,name="edit_card"),

    path("receipts/<int:id>/",receipt_profile,name="receipt_profile"),
    path("receipts/edit/<int:id>/",edit_receipt,name="edit_receipt"),
    
    path("transactions/<int:id>/",transaction_profile,name="transaction_profile"),
    path("transactions/edit/<int:id>/",edit_transaction,name="edit_transaction"),

]

   

