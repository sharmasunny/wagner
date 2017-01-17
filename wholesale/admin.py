from django.contrib import admin

# Register your models here.
from .models import Order, Product, OrderItem, ColourClass, ProductCategory, NewRelease, UserInfo


class ProductAdmin(admin.ModelAdmin):
    list_display = ["list_no", "__str__", "category_id"]

    class Meta:
        model = Product


admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem)
admin.site.register(ColourClass)
admin.site.register(ProductCategory)
admin.site.register(NewRelease)
admin.site.register(UserInfo)


