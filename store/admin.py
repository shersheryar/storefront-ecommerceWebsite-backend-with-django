from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Collection)
admin.site.register(models.Product)
admin.site.register(models.Promotion)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
# admin.site.register(models.TaggedItem)
# admin.site.register(models.ProductTag)
# admin.site.register(models.Tag)
