from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.db import models
from django.utils import timezone

class SalesChannel(models.Model):
    """
    Represents a sales channel from which orders can be imported.
    """
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)
    # other fields as needed

    def __str__(self):
        return self.name

class Order(models.Model):
    """
    Represents an order imported from a sales channel.
    """
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('cancelled', 'Cancelled'),
    ]

    order_number = models.CharField(max_length=100, unique=True)
    sales_channel = models.ForeignKey(SalesChannel, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    shipping_address = models.CharField(max_length=200)
    shipping_method = models.CharField(max_length=50)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    # label = models.CharField(_("Label"), max_length=100, null=True, blank=True)
    label = models.ImageField(_("Label"), null=True, blank=True)

    # other fields as needed

    def __str__(self):
        return self.order_number

class Courier(models.Model):
    """
    Represents a courier used to ship orders.
    """
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    # other fields as needed

    def __str__(self):
        return self.name

class ShippingRule(models.Model):
    """
    Represents a shipping rule used to automate shipping processes.
    """
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    delivery_speed = models.CharField(max_length=50)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2)
    # other fields as needed

    def __str__(self):
        return f'{self.courier.name} - {self.delivery_speed} - {self.shipping_cost}'

class Shipment(models.Model):
    """
    Represents a shipment created when an order is shipped.
    """
    shipment_status_choices = [
        ('created', 'Created'),
        ('shipped', 'Shipped'),
        ('cancelled', 'Cancelled'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100, unique=True)
    shipment_status = models.CharField(max_length=20, choices=shipment_status_choices, default='created')
    shipped_date = models.DateTimeField(default=timezone.now)
    # other fields as needed

    def __str__(self):
        return self.tracking_number
    
    