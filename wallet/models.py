
from datetime import datetime
from email import message
from locale import currency
from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(null=True,max_length=100)
    last_name = models.CharField(null=True,max_length=100)
    address = models.TextField(null=True,max_length=50)
    email = models.EmailField(null=True,max_length=150)
    phonenumber =models.CharField (max_length=16)
    age = models.IntegerField(null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)
    nationality=models.CharField(max_length=20,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True)



class Wallet(models.Model):
    customer = models.ForeignKey(default=1,on_delete=models.CASCADE, to = Customer)
    currency = models.CharField(max_length=50)
    pin = models.PositiveSmallIntegerField()
    date_created = models.DateTimeField(default=datetime.now)
    isActive = models.BooleanField()
    balance = models.BigIntegerField()
   


class Account(models.Model):
    account_number = models.IntegerField()
    account_name = models.CharField(max_length=100)
    wallet = models.ForeignKey(default=1,on_delete=models.CASCADE, to=Wallet)
    balance = models.PositiveIntegerField()
    account_type = models.CharField(max_length=100)

    def deposit(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
       else:
           self.account_balance += amount
           self.save()
           message = f"You have deposited {amount}, your new balance is {self.account_balance}"
           status = 200
       return message, status

    
    def transfer(self, destination, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
      
       elif amount > self.account_balance:
           message =  "Insufficient balance"
           status = 403
      
       else:
           self.account_balance -= amount
           self.save()
           destination.deposit(amount)
          
           message = f"You have transfered {amount}, your new balance is {self.account_balance}"
           status = 200
       return message, status


    def withdraw(self,amount):
        date = datetime.now()
        if amount <= 0:
            message = f"Enter the correct amount"
            status = 403
            return  message, status
        elif amount > self.account_balance:
            message=  f"your account balance is low "
            status = 403
            return message, status
        else: 
           self.account_balance -= amount
           message = f"Hello {self.account_name} you have withdrawn {amount} at {date.strftime('%d%Y/%m/ %H:%M')} and your balance is {self.account_balance}"
           status = 200
           return message, status
        

    def borrow(self,amount):
        self.loan_balance = 0
        if amount <= 100:
            message = f"Enter amount more than 100"
            status = 403
            return message , status
        elif self.loan_balance > 0:
            message = f"You have an outstanding amount of {self.loan_balance}"
            status = 403
            return message , status
        else:
            self.loan_balance += amount
            self.account_balance += amount
            message = f"Your loan balance is {self.loan_balance}"
            status = 200
            return message , status
    

    def loan_repayment(self, amount):

        if amount < self.loan_balance:
            self.loan_balance -= amount
            message =  f"You have paid {amount} and your have an outstanding balance of {self.loan_balance}"
            status = 403
            return message , status

        elif amount == self.loan_balance:
            self.loan_balance-= amount
            message = f"You have paid {amount} and your have an outstanding balance of {self.loan_balance}"
            status = 403
            return message, status
        elif self.loan_balance == 0:
            message = f"You have no loan balance, you can borrow"
            status = 403
            return message, status

        else:   
            overpay = amount - self.loan_balance
            self.account_balance+=overpay
            self.loan_balance = 0
            message = f"You loan has been fully settled."
            status = 200
            return message, status
   


class Transaction(models.Model):
    transaction_code = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=100)
    transaction_charge = models.IntegerField()
    transaction_number = models.IntegerField()
    transaction_amount = models.BigIntegerField()
    message = models.CharField(max_length=100)
    origin_account =models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name='origin_transaction',null=True)
    destination_account = models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name='destination_transaction',null=True)


class Card(models.Model):
    card_name  = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    expiry_date = models.DateTimeField(default=datetime.now)
    issuer = models.CharField(max_length=100)
    account = models.ForeignKey(default=1,on_delete=models.CASCADE, to=Account)
    date_issued = models.DateTimeField(default=datetime.now)


class ThirdParty(models.Model):
    third_party_name = models.CharField(max_length=100)
    transaction_cost = models.IntegerField()
    currency = models.CharField(max_length=100)
    account = models.ForeignKey(default=1,on_delete=models.CASCADE, to=Account)
    thirdparty_id=models.CharField(max_length=10,null=True)
    phone_Number=models.IntegerField()


class Notification(models.Model):
    message = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
   

class Receipt(models.Model):
    amount = models.IntegerField()
    dateTime = models.DateTimeField(default=datetime.now)
    receipt_message = models.CharField(max_length=100)

class Loan(models.Model):
    Wallet = models.ForeignKey(default=1,on_delete=models.CASCADE, to=Wallet)
    interest_rate = models.IntegerField()
    loan_balance = models.IntegerField()
    loanTerm = models.IntegerField()
    payment_due_date = models.DateTimeField(default=datetime.now)
    purpose = models.CharField(max_length=100)
    amount = models.IntegerField()

class Reward(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()
    customer_id = models.IntegerField()   
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)  
    bonus=models.CharField(max_length=25, null=True) 




 
