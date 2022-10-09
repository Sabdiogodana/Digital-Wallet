from django.urls import path, include
from rest_framework import routers
from wallet.models import Customer
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
]
