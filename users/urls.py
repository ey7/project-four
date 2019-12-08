from django.urls import path
from . views import register, account

urlpatterns = [
	path('register/', register, name="register"),
	path('account/', account, name="account"),
]
