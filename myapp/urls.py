from django.urls import path
from myapp import views

urlpatterns=[
    path('index_page/',views.index_page,name='index_page'),
    path('category/',views.category,name='category'),
    path('categorydata/',views.categorydata,name='categorydata'),
    path('categorydisplay/',views.categorydisplay,name='categorydisplay'),
    path('edit_category/<int:dataid>/',views.edit_category,name='edit_category'),
    path('update_category/<int:dataid>/',views.update_category,name='update_category'),
    path('delete_category/<int:dataid>/',views.delete_category,name='delete_category'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('productdata/',views.productdata,name='productdata'),
    path('productdisplay/',views.productdisplay,name='productdisplay'),
    path('editproduct/<int:dataid>/',views.editproduct,name='editproduct'),
    path('updateproduct/<int:dataid>/',views.updateproduct,name='updateproduct'),
    path('delete_product/<int:dataid>/',views.delete_product,name='delete_product'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('contactdisplay/',views.contactdisplay,name='contactdisplay'),
    path('delete_contactus/<int:dataid>/',views.delete_contactus,name='delete_contactus'),

]