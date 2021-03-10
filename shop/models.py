from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    parent_category=models.ForeignKey('self', related_name='categories', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique= True)
    image = models.ImageField(upload_to='categories/', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class AttributeBase(models.Model):
    label = models.CharField(max_length=255, null=True) # e.g. color, size, shape, etc.

    def __str__(self):
        return self.label
    
    def __lt__(self, other):
        return self.__str__() < other.__str__()

    

class Attribute(models.Model):
    base = models.ForeignKey('AttributeBase', related_name='attributes', on_delete=models.CASCADE)
    value = models.CharField(max_length=255) # e.g. red, L, round, etc.

    
class ProductAttribute(Attribute):
    product_type = models.ForeignKey('ProductType', related_name='attributes', null=True, on_delete=models.CASCADE)

    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name = 'products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    # description = models.TextField(blank=True)
    description = HTMLField()
    PDF = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['pdf'])], upload_to='pdf/fiches techniques/')

    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # available = models.BooleanField(default=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    

class ProductType(models.Model):
    product = models.ForeignKey(Product, related_name = 'types', on_delete=models.CASCADE)
    reference = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('product',)

    def __str__(self):
        return self.reference
    
    