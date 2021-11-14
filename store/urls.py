from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . views import *
from . import views

app_name = 'store'

urlpatterns = [
	#Leave as empty string for base url
	
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	# path('home/', include('home.urls')),

]