
from atexit import register
from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
    
admin.site.register(Customer) 
admin.site.register(Wallet) 
admin.site.register(Account) 
admin.site.register(Transaction)
admin.site.register(Card) 
admin.site.register(ThirdParty) 
admin.site.register(Notification,) 
admin.site.register(Receipt) 
admin.site.register(Loan)
admin.site.register(Reward) 