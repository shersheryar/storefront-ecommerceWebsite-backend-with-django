from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models.aggregates import Count
from django.http import HttpRequest
from . import models
# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory_status', 'collection_title']
    list_editable = ['price']
    list_per_page = 10
    search_fields = ['title', 'description']
    list_filter = ['last_update', 'collection']
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        else:
            return 'Ok'


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    list_filter = ['first_name', 'membership']
    ordering = ['first_name', 'last_name']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']

    # def customer_name(self, order):
    #     return


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products_count

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )


    # second approach to register the model
    # admin.site.register(models.Collection)
    # admin.site.register(models.Product, ProductAdmin)
    # admin.site.register(models.Customer)
    # admin.site.register(models.Promotion)
    # admin.site.register(models.Order)
    # admin.site.register(models.OrderItem)
    # admin.site.register(models.TaggedItem)
    # admin.site.register(models.ProductTag)
admin.site.register(models.Promotion)
