from django.urls import path
from . import views




urlpatterns = [
    path('',views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='prod_cart'),
    path('<slug:c_slug>/<slug:products_slug>',views.prodDetails,name='details'),
    path('search',views.searching,name='search'),
]





