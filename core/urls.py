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
    path("checkout", views.checkout),
    path("update_item", views.updateItem, name='update_item'),
]