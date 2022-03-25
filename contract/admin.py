from django.contrib import admin

from contract.models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'value',
     'payment_deadline', 'status', 'saler',
     'customer')
    list_filter = ('customer',)
    search_fields = ('name',)

