from django.urls import path, include
from rest_framework import routers
from wallet.models import Customer
from rest_framework import views
from .views import AccountViewset, CardViewset, CustomerViewSet, LoanViewset, NotificationViewset, ReceiptViewSet, ThirdpartyViewset, TransactionViewset, WalletViewset


router =  routers.DefaultRouter()
router.register(r"customers", CustomerViewSet,basename=Customer)
router.register (r"accounts", AccountViewset)
router.register (r"wallets", WalletViewset)
router.register (r"cards", CardViewset)
router.register (r"loans", LoanViewset)
router.register (r"notifications", NotificationViewset)
router.register (r"receipts", ReceiptViewSet)
router.register (r"rewards", ReceiptViewSet)
router.register (r"thirdparties", ThirdpartyViewset)
router.register (r"transactions", TransactionViewset)


urlpatterns = [
    path("",include(router.urls)),
    path("deposit/", views.AccountDepositView.as_view(), name="deposit-view"),
    path("deposit/<int:id>/", views.AccountDepositView.as_view(), name="deposit-view"),
    path("transfer/<int:id>/", views.AccountTransferView.as_view(), name="transfer-view"),
    path("withdrawal/",views.AccountWithdrawalView.as_view(),name="withrawal-view"),
    path("loan_request/",views.AccountLoanRequestView.as_view(),name="loan-view"),
    path("loan_repayment/",views.AccountLoanRepaymentView.as_view(),name="repay-loan-view"),

]
