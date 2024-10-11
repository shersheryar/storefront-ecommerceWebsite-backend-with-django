from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_editable = ['price']
    list_per_page = 10
    search_fields = ['title', 'description']
    list_filter = ['last_update', 'collection']


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    list_filter = ['first_name', 'membership']
    ordering = ['first_name', 'last_name']


# second approach to register the model
# admin.site.register(models.Collection)
# admin.site.register(models.Product, ProductAdmin)
# admin.site.register(models.Customer)
# admin.site.register(models.Promotion)
# admin.site.register(models.Order)
# admin.site.register(models.OrderItem)
# admin.site.register(models.TaggedItem)
# admin.site.register(models.ProductTag)
# admin.site.register(models.Tag)
