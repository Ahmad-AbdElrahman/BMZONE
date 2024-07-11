from django.db import models
from django.contrib.auth.models import User
# Create your models here .

class Customer(models.Model): 
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, max_length=200, null=False)
    name = models.CharField(max_length=200)

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS =  ['username']

    def __str__(self):
        return self.name 

class Vendor(models.Model): 
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, max_length=200, null=False)
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name 

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)
    review = models.IntegerField(default=0)
    price = models.FloatField()
    description = models.TextField(max_length=500, null=True, blank=True)
    digital = models.BooleanField(default=False, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name 
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id) 
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def service(self):
        service = self.get_cart_total * 0.1
        return service
    
    @property
    def gross_total(self):
        total = self.get_cart_total + self.service
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    # def __str__(self):
    #     return str(self.id) 

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    zipcode = models.CharField(max_length=100, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address 
