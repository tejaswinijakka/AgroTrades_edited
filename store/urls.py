from django.contrib import admin
from django.urls import path
from .views.view import etrade, crop_pred, predict, index
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views import base2

urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('etrade',etrade, name='etrade'),
    path('crop_prediction',crop_pred,name='croppredpage'),
    path('predict',predict, name='predict'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('store', store , name='store'),
    #path('base2', base2.as_view(), name = 'base2'),
]
