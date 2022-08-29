
from atexit import register
from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

class CustomerAdmin(admin.ModelAdmin):
    list_display =("first_name","last_name","address","email","age",)
    search_fields = ("first_name", "last_name","adress","email","age",)
admin.site.register(Customer,CustomerAdmin) 

class WalletAdmin(admin.ModelAdmin):
   list_display =("balance","currency","pin","isActive","date_created")
   search_fields = ("balance", "currency","pin","isActive","date_created") 
admin.site.register(Wallet,WalletAdmin) 

class AccountAdmin(admin.ModelAdmin):
   list_display =("account_number","account_name","wallet","balance","account_type",)
   search_fields = ("account_number","account_name","wallet","balance","account_type",)
admin.site.register(Account,AccountAdmin) 

# class TransactionAdmin(admin.ModelAdmin):
#    list_display =("account_number","account_name","wallet","balance","account_type",)
#    search_fields = ("account_number","account_name","wallet","balance","account_type",)
admin.site.register(Transaction)

class CardAdmin(admin.ModelAdmin):
   list_display =("card_name","card_number","account","issuer","expiry_date","date_issued")
   search_fields = ("card_name","card_number","account","issuer","expiry_date","date_issued")
admin.site.register(Card,CardAdmin) 

class ThirdPartyAdmin(admin.ModelAdmin):
   list_display =("third_party_name","transaction_cost","currency","account","thirdparty_id","phone_Number")
   search_fields = ("third_party_name","transaction_cost","currency","account","thirdparty_id","phone_Number")
admin.site.register(ThirdParty,ThirdPartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
   list_display =("message","title",)
   search_fields = ("message","title",)
admin.site.register(Notification,NotificationAdmin) 

class ReceiptAdmin(admin.ModelAdmin):
   list_display =("amount","dateTime","receipt_message",)
   search_fields = ("amount","dateTime","receipt_message",)
admin.site.register(Receipt,ReceiptAdmin) 

class LoanAdmin(admin.ModelAdmin):
   list_display =("interest_rate","loan_balance","loanTerm","payment_due_date","purpose","amount")
   search_fields = ("interest_rate","loan_balance","loanTerm","payment_due_date","purpose","amount")
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
   list_display =("name","points","customer_id","gender","bonus",)
   search_fields = ("name","points","customer_id","gender","bonus",)
admin.site.register(Reward,RewardAdmin) 

