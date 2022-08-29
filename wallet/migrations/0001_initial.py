# Generated by Django 4.0.6 on 2022-08-25 04:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('account_name', models.CharField(max_length=100)),
                ('balance', models.PositiveIntegerField()),
                ('account_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=150, null=True)),
                ('phonenumber', models.CharField(max_length=16)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('nationality', models.CharField(max_length=20, null=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='profile_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('dateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('receipt_message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
                ('customer_id', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('bonus', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=50)),
                ('pin', models.PositiveSmallIntegerField()),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('isActive', models.BooleanField()),
                ('balance', models.BigIntegerField()),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.CharField(max_length=100)),
                ('transaction_type', models.CharField(max_length=100)),
                ('transaction_charge', models.IntegerField()),
                ('transaction_number', models.IntegerField()),
                ('transaction_amount', models.BigIntegerField()),
                ('message', models.CharField(max_length=100)),
                ('destination_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination_transaction', to='wallet.wallet')),
                ('origin_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_transaction', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('third_party_name', models.CharField(max_length=100)),
                ('transaction_cost', models.IntegerField()),
                ('currency', models.CharField(max_length=100)),
                ('thirdparty_id', models.CharField(max_length=10, null=True)),
                ('phone_Number', models.IntegerField()),
                ('account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_rate', models.IntegerField()),
                ('loan_balance', models.IntegerField()),
                ('loanTerm', models.IntegerField()),
                ('payment_due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('purpose', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('Wallet', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=100)),
                ('card_number', models.CharField(max_length=100)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime.now)),
                ('issuer', models.CharField(max_length=100)),
                ('date_issued', models.DateTimeField(default=datetime.datetime.now)),
                ('account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet'),
        ),
    ]
