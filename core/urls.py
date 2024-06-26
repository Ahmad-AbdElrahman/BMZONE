from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about),
    path("sproduct", views.sproduct),
    path("contact", views.contact),
    path("cart", views.cart),
    path("shop", views.shop),
]