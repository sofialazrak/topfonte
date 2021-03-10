from django.contrib import admin
from .models import Category, Product, ProductType, AttributeBase, ProductAttribute


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = (        
         'parent_category',
         'name',
         'slug',
         'image',
    )
    prepopulated_fields = {'slug' : ('name',)}

    # class Media:
    #     js = (
    #         'js/myscript.js',  
    #     )
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['reference', 'product','price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']

@admin.register(AttributeBase)
class AttributeBaseAdmin(admin.ModelAdmin):
    list_display = ['label']

@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['product_type','base', 'value']
    list_filter = ['product_type']
    