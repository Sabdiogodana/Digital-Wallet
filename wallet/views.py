
from urllib import request
from django.shortcuts import redirect, render

from wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
from .forms import CustomerRegistrationForm
from .forms import WalletRegistrationForm
from .forms import AccountRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import CardRegistrationForm
from .forms import ThirdPartyRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import ReceiptRegistrationForm
from .forms import LoanRegistrationForm
from .forms import RewardRegistrationForm



def register_customer(request):
    if request.method =="POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
       
        form  = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})

def list_customer(request):
    customers = Customer.objects.all()
    return render(request,"wallet/customer_list.html",{"customers":customers})

    # Single Object view
# def wallet_profile(request,id):
#     wallet = Wallet.objects.get(id=id)
#     return render(request,"wallet/wallet_profile.html",{"wallet":wallet})

# def edit_profile(request,id):
#     wallet = Wallet.objects.get(id=id)
#     if request.method=="POST":
#         form = WalletRegistrationForm(request.POST,instance=Wallet)
#         if form.isvalid():
#             form.save()
#             return redirect("wallet_profile",id=wallet.id)
#     else:
#         form = WalletRegistrationForm(instance=Customer)
#         return render(request,"wallet/edit_profile.html",{"form":form})


            



def register_wallet(request):
    if request.method =="POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form = WalletRegistrationForm()   
            return render(request,"wallet/register_wallet.html",{"form":form}) 
               
def list_wallet(request):
    wallets = Wallet.objects.all()
    return render(request,"wallet/wallet_list.html",{"wallets":wallets})

    # Single Object view
def customer_profile(request,id):
    customer = Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",{"customer":customer})

def edit_profile(request,id):
    customer = Customer.objects.get(id=id)
    if request.method=="POST":
        form = CustomerRegistrationForm(request.POST,instance=Customer)
        if form.isvalid():
            form.save()
            return redirect("Customer_profile",id=customer.id)
    else:
        form = CustomerRegistrationForm(instance=Customer)
        return render(request,"wallet/edit_profile.html",{"form":form})


            


def register_account(request):
    if request.method =="POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form  = AccountRegistrationForm()
        return render(request,"wallet/register_account.html", {"form":form})  
def list_account(request):
    accounts = Account.objects.all()
    return render(request,"wallet/account_list.html",{"accounts":accounts})
            
          


def register_transaction(request):
    if request.method =="POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form  = TransactionRegistrationForm()
            return render(request,"wallet/register_transaction.html",{"form":form})     
def list_transaction(request):
    transactions = Transaction.objects.all()
    return render(request,"wallet/transaction_list.html",{"transactions":transactions})
            

def register_card(request):
    if request.method =="POST":
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form  = CardRegistrationForm()
            return render(request,"wallet/register_card.html",{"form":form})  
def list_card(request):
    cards = Card.objects.all()
    return render(request,"wallet/card_list.html",{"cards":cards})
            
                       


def register_thirdparty(request):
    if request.method =="POST":
        form = ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form  = ThirdPartyRegistrationForm()
            return render(request,"wallet/register_thirdparty.html",
            {"form":form})     
def list_thirdparty(request):
    thirdparties = ThirdParty.objects.all()
    return render(request,"wallet/thirdparty_list.html",{"thirdparties":thirdparties})
            

def register_notification(request):
    if request.method =="POST":
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form  = NotificationRegistrationForm()
            return render(request,"wallet/register_notification.html",
            {"form":form})    
def list_notification(request):
    notifications = Notification.objects.all()
    return render(request,"wallet/notification_list.html",{"notifications":notifications})
                      


def register_receipt(request):
    if request.method =="POST":
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form  = ReceiptRegistrationForm()
            return render(request,"wallet/register_receipt.html",
            {"form":form})   
def list_receipt(request):
    receipts = Receipt.objects.all()
    return render(request,"wallet/receipt_list.html",{"receipts":receipts})
                    


def register_loan(request):
    if request.method =="POST":
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form  = LoanRegistrationForm()
            return render(request,"wallet/register_loan.html",
            {"form":form})  
def list_loan(request):
    loans = Loan.objects.all()
    return render(request,"wallet/loan_list.html",{"loans":loans})
                    

   

def register_reward(request):
    if request.method =="POST":
        form =RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form  = RewardRegistrationForm()
            return render(request,"wallet/register_reward.html",
            {"form":form})   
def list_reward(request):
    rewards = Reward.objects.all()
    return render(request,"wallet/reward_list.html",{"rewards":rewards})
                    
# # Single Object view
def customer_profile(request,id):
    customer = Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",{"customer":customer})

def edit_profile(request,id):
    customer = Customer.objects.get(id=id)
    if request.method=="POST":
        form = CustomerRegistrationForm(request.POST,instance=Customer)
        if form.isvalid():
            form.save()
            return redirect("Customer_profile",id=customer.id)
    else:
        form = CustomerRegistrationForm(instance=Customer)
        return render(request,"wallet/edit_profile.html",{"form":form})


# Create your views here.
def wallet_profile(request,id):
    wallet = Wallet.objects.get(id=id)
    return render(request, 'wallet/wallet_profile.html',{'wallet': wallet})

def edit_wallet(request,id):
    wallet= Wallet.objects.get(id=id)
    if request.method =="POST":
        form= WalletRegistrationForm(request.POST,instance=Wallet)
        if form.is_valid():
            form.save()
            return redirect("wallet_profile",id=wallet.id)
    else:
        form=WalletRegistrationForm(instance=Wallet)
        return render(request,"wallet/edit_wallet.html",{"form":form})


def account_profile(request,id):
    account = Account.objects.get(id=id)
    return render(request, 'wallet/account_profile.html',{'account': account})

def edit_account(request,id):
    account=Account.objects.get(id=id)
    if request.method =="POST":
        form=AccountRegistrationForm(request.POST,instance=Account)
        if form.is_valid():
            form.save()
            return redirect("account_profile",id=account.id)
    else:
        form=AccountRegistrationForm(instance=Account)
        return render(request,"wallet/edit_account.html",{"form":form})


def card_profile(request,id):
    card = Card.objects.get(id=id)
    return render(request, 'wallet/card_profile.html',{'card': card})

def edit_card(request,id):
    card=Card.objects.get(id=id)
    if request.method =="POST":
        form=CardRegistrationForm(request.POST,instance=Card)
        if form.is_valid():
            form.save()
            return redirect("card_profile",id=card.id)
    else:
        form=CardRegistrationForm(instance=Card)
        return render(request,"wallet/edit_card.html",{"form":form})

def edit_receipt(request,id):
    card=Receipt.objects.get(id=id)
    if request.method =="POST":
        form=ReceiptRegistrationForm(request.POST,instance=Receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt_profile",id=card.id)
    else:
        form=CardRegistrationForm(instance=Receipt)
        return render(request,"wallet/edit_receipt.html",{"form":form})

def transaction_profile(request,id):
    transaction = Transaction.objects.get(id=id)
    return render(request, 'wallet/transaction_profile.html',{'transaction': transaction})


def edit_transaction(request,id):
    transaction=Transaction.objects.get(id=id)
    if request.method =="POST":
        form=TransactionRegistrationForm(request.POST,instance=Transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_profile",id=transaction.id)
    else:
        form=TransactionRegistrationForm(instance=Transaction)
        return render(request,"wallet/edit_transaction.html",{"form":form})

