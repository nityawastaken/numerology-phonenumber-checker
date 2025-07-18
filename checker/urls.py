from django.urls import path
from .views import *


urlpatterns = [
#     path('checker/', index, name='index'),
#     path('', home_view, name='home'),
#     path('signup/', signup_view, name='signup'),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
#     path('upload-payment/', payment_view, name='upload_payment'),
    path('',home_view, name='home'),
    path('index/', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('payment/', payment_view, name='payment'),
]