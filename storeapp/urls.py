from django.urls import path
from .views import *


urlpatterns = [
    path('', Homepage.as_view()),
    path('cart/', CartPage.as_view()),
    path('add/<int:id>/', Add_To_Cart.as_view(), name='add_to_cart'),
    path('remove/<int:id>/', Remove_From_Cart.as_view(), name='remove_from_cart'),
    path('increase/<int:id>/', Increase_Quantity.as_view(), name='increase'),
    path('decrease/<int:id>/', Decrease_Quantity.as_view(), name='decrease'),
    path('orderplace/' ,Place_Order.as_view()),
    path('login/', Login.as_view()),
    path('signup/', Signup.as_view()),
]