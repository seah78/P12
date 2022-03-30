from django.contrib import admin

from account.models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'first_name', 'last_name', 
                    'email', 'seller')
    list_filter = ('seller',)
    search_fields = ('company_name', 'seller',)
