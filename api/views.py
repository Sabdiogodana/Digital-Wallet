from django.shortcuts import render
from httplib2 import Response
from rest_framework import viewsets
from wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
from .serializer import AccountSerializer, CardSerializer, CustomerSerializer, LoanSerializer, NotificationSerializer, ReceiptSerializer, RewardSerializer, ThirdpartySerializer, TransactionSerializer, WalletSerializer
from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist




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

# deposite
class AccountDepositView(views.APIView):
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)

   def get(self,request,id,format=None):
    account_id = Account.objects.get(id=id)
    if request.method == 'GET':
        serializer_account = serializers.AccountSerializer(account_id)
        return Response(serializer_account.data)


# Transfer
class AccountTransferView(views.APIView):
    def post(self, request, id, format=None):       
       account_id = request.data["destination_account"]
       amount = request.data["amount"]
       origin_account = Account.objects.get(id = id)
       try:
           account = Account.objects.get(id= account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = origin_account.transfer(account,amount)
       return Response(message, status=status)
# loan request
class AccountLoanRequestView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)    
        except ObjectDoesNotExist:  
            return Response("Account Not Found", status=404)
        message, status = account.borrow(amount) 
        return Response (message,status=status)
# loan repayment
class AccountLoanRepaymentView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)    
        except ObjectDoesNotExist:  
            return Response("Account Not Found", status=404)
        message, status = account.loan_repayment(amount) 
        return Response (message,status=status)

# Withdraw
class AccountWithdrawalView(views.APIView):
    def post(self,request,pk,format=None):
        account_id=request.data["account_id"]    
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)    
        except ObjectDoesNotExist: 
            return Response("Account Not Found", status=404)
        message, status = account.withdraw(amount) 
        return Response (message,status=status)
