from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='Addcart'),
    path('', views.cart_detail,name='cart_detail'),
    path('remove/<int:product_id>/',views.remove,name='ItemRemove'),
    path('delete/<int:product_id>/',views.deletion, name='Deletion'),


]