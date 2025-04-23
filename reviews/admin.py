from django.contrib import admin
from .models import UserRegister,Review,Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('slug',)
    list_display = ('product_name', 'category')

admin.site.register(Product,ProductAdmin)
admin.site.register(UserRegister)
admin.site.register(Review)