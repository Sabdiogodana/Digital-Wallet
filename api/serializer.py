from dataclasses import fields
from wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta :
        model = Customer
        fields = ("first_name","last_name","email","address","email","age",)

class  WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model= Wallet
        fields=("isActive","balance","customer","pin","currency","date_created")
    

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model= Account
        fields=("account_number","account_name","account_type","balance","wallet")

class  CardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Card
        fields=("card_number","card_name","date_issued","expiry_date","account","issuer")   

class  LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model= Loan
        fields=("amount","Wallet","loanTerm","payment_due_date","loan_balance","interest_rate","purpose")      


class  NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Notification
        fields=("message","title")

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model= Receipt
        fields=("amount","dateTime","receipt_message")
                     

class  RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reward
        fields=("name","points","customer_id","gender","bonus")  



class  ThirdpartySerializer(serializers.ModelSerializer):
    class Meta:
        model= ThirdParty
        fields=("account","currency","phone_Number","thirdparty_id","transaction_cost","third_party_name") 

class  TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transaction
        fields=("transaction_code","transaction_type","transaction_charge","transaction_number","transaction_cost","destination_account","origin_account","message")                  