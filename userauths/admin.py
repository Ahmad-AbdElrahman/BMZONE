from django.contrib import admin
from userauths.models import * 
# Register your models here.

admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)