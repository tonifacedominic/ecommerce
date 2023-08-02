
from django.urls import path
from ecommerceapp import views
app_name='ecommerce'

urlpatterns = [

    path('',views.AllProdCat,name='AllProdCat'),
    path('<slug:c_slug>/',views.AllProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.ProDetail,name='Product_details'),

]
