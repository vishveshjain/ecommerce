from .models import billingAddress, productData
from django.contrib import admin

# Register your models here.
admin.site.register(productData)
admin.site.register(billingAddress)