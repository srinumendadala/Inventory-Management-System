from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cust/', views.addCustomer, name='addCustomer'),
    path('custSearch/', views.customerSearch, name='custSearch'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('cat/', views.addCategory, name='addCategory'),
    path('catSearch/', views.categorySearch, name='catSearch'),
    path('deletecat/<int:pk>', views.deletecat, name='deletecat'),
    path('brand/', views.addBrand, name='addBrand'),
    path('deltbrand/<int:pk>', views.deletebrand, name='deltbrand'),
    path('supply/', views.addSupplier, name='supplier'),
    path('delsupplier/<int:pk>', views.deletesupplier, name='delsupplier'),
    path('product/', views.addProduct, name='products'),
    path('delproduct/<int:pk>', views.deleteproduct, name='delprod'),
    path('purch/', views.addPurchase, name='purchase'),
    path('delpurch/<int:pk>', views.deletepurchase, name='delpurch'),
    path('manage/', views.manage, name='manage'),
    path('delmana/<int:pk>', views.deleteorder,  name='delorder'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update_customer/<int:id>', views.update_customer, name='update_customer'),
    path('updateCategory/<int:id>', views.updateCategory, name='updateCategory'),
    path('updateSupplier/<int:id>', views.updateSupplier, name='updateSupplier'),
]