from django.contrib import admin
from .models import *

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('Customer', 'due_date', 'total_amount', 'is_paid') # 'customer_email',
    search_fields = ('Customer', 'due_date') # , 'customer_email'
    list_filter = ('is_paid', )
admin.site.register(Customer)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Product)
admin.site.register(Expense)
admin.site.register(GSTInvoice)
admin.site.register(Payment)
admin.site.register(Vendor)
""" admin.site.register(CustomUser) """