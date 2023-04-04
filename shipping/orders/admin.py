from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
# Register your models here.
from django.contrib import admin

from .models import SalesChannel, Order, Courier, ShippingRule, Shipment

from barcode import EAN13
from barcode.writer import ImageWriter

@admin.register(SalesChannel)
class SalesChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'api_key')
    search_fields = ('name',)



        
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_number',
        'sales_channel',
        'order_date',
        'customer_name',
        'customer_email',
        'shipping_address',
        'shipping_method',
        'order_status',
        'label',
        
    )
    
    @admin.action(description="Generate label for selected Orders")
    def generate_label(self, request, queryset):
        
        for order in queryset:
            number = '59012341234'
            id  = str(order.id)
            print(len(id))
            if len(id)<2:
                number1 = number + '0' + id 
            else:
                number1 = number + id
            
            print(number1)
            my_code = EAN13(number1, writer=ImageWriter())
            path = f"media/{number1}"
            my_code.save(path)
            order.label = number1 + ".png"
            order.save()
        

        # self.message_user(request, ngettext('%d Label was successfully marked as published.','%d Labels were successfully marked as published.',updated,) % updated, messages.SUCCESS)
    actions =[generate_label]
    
    list_filter = ('sales_channel', 'order_date')
    search_fields = ('sales_channel', 'order_date')

    


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'account_number')
    search_fields = ('name',)


@admin.register(ShippingRule)
class ShippingRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'courier', 'delivery_speed', 'shipping_cost')
    # list_filter = ('courier',)


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'courier',
        'tracking_number',
        'shipment_status',
        'shipped_date',
    )
    # list_filter = ('order', 'courier', 'shipped_date')