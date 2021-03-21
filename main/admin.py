from django.contrib import admin
from .models import Category,Brand,Color,Size,Product,ProductAttribute,Banner



admin.site.register(Size)
admin.site.register(Banner)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title' , 'Category_image')
admin.site.register(Category,CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('title' , 'Brand_image')
admin.site.register(Brand,BrandAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title' , 'Color_bg')
admin.site.register(Color,ColorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' , 'brand' , 'status' , 'is_featured','Product_image')
    list_editable = ('status','is_featured')
admin.site.register(Product,ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id' , 'product' , 'price' , 'color' , 'size' )
admin.site.register(ProductAttribute,ProductAttributeAdmin)


