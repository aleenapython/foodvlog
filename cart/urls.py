from django.urls import path
from . import views



urlpatterns=[
    path('cartDetails',views.cart_details,name='cartDetaild'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
     path('dic/<int:product_id>/',views.min_cart,name='cart_decrement'),
      path('delete/<int:product_id>/',views.cart_delete,name='remove')
]