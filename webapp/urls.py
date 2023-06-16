from django.urls import path
from webapp import views
urlpatterns=[

    path('home/', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('categories/<catname>', views.categories, name='categories'),
    path('singleproduct/<int:dataid>/', views.singleproduct, name='singleproduct'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userdata/', views.userdata, name='userdata'),
    path('usersignin/', views.usersignin, name='usersignin'),
    path('contactdata/', views.contactdata, name='contactdata'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('cartpage/', views.cartpage, name='cartpage'),
    path('cartdata/', views.cartdata, name='cartdata'),
    path('checkoutpage/', views.checkoutpage, name='checkoutpage'),


]
