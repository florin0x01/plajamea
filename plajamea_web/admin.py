from django.contrib import admin

from .models import *

admin.site.register(Umbrella)
admin.site.register(Table)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Waiter)
admin.site.register(WaitedTables)
admin.site.register(OrderProduct)

# Register your models here.
