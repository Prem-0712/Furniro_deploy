from django.urls import path
from core import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("shop/", views.shop, name="shop"), 
    path("single_product/<int:id>", views.single_product, name="single"),
    path('chair_categories/', views.chair_categories, name='chair'),
    path('sofa_categories/', views.sofa_categories, name='sofa'),
    path('table_categories/', views.table_categories, name='table'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.log_in, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.log_out, name='logout'),
    path('changepassword/', views.changepassword, name='changepass'),
    path('view_cart/',views.view_cart, name="viewcart"),
    path('add_to_cart/<int:id>',views.add_to_cart, name="addtocart"),
    path('add_quantity/<int:id>',views.add_quantity, name="add_quantity"),
    path('delete_quantity/<int:id>',views.delete_quantity, name="delete_quantity"),
    path('delete_cart/<int:id>',views.delete_cart, name="deletecart"),
    path('address/',views.address,name='address'),
    path('delete_address/<int:id>',views.delete_address,name='deleteaddress'),
    path('checkout/',views.checkout,name='checkout'),
    path('payment_success/<int:selected_address_id>',views.payment_success,name='paymentsuccess'),
    path('payment_failed/',views.payment_failed,name='paymentfailed'),
    path('payment/',views.payment,name='payment'),
    path('order/',views.order,name='order'),
    path('buynow/<int:id>',views.buynow,name='buynow'),
    path('buynow_payment/<int:id>',views.buynow_payment,name='buynowpayment'),
    path('buynow_payment_success/<int:selected_address_id>/<int:id>',views.buynow_payment_success,name='buynowpaymentsuccess'),
]

if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)