from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
from .serializer import AccountSerializer, CardSerializer, CustomerSerializer, LoanSerializer, NotificationSerializer, ReceiptSerializer, RewardSerializer, ThirdpartySerializer, TransactionSerializer, WalletSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class WalletViewset(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class=WalletSerializer   

class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class=AccountSerializer 



class CardViewset(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class=CardSerializer


class LoanViewset(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class=LoanSerializer


class NotificationViewset(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class=NotificationSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class=ReceiptSerializer
       
   
class RewardViewset(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class=RewardSerializer


class ThirdpartyViewset(viewsets.ModelViewSet):
    queryset = ThirdParty.objects.all()
    serializer_class=ThirdpartySerializer


class TransactionViewset(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class=TransactionSerializer
