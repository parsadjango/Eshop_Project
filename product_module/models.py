from django.db import models
# from django.core import validators
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class ProductBrand(models.Model):
    title = models.CharField(max_length=200, verbose_name="Brand Name", db_index=True)
    is_active = models.BooleanField(verbose_name="Active/Not Active")

    class Meta:
        verbose_name = "Brands"
        verbose_name_plural = "Brand Name"

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name="title", db_index=True)
    url_title = models.CharField(max_length=200, verbose_name="URL in Title", db_index=True)

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    category = models.ManyToManyField(ProductCategory, related_name='products_categories')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='Brand Name', null=True)
    image = models.ImageField(upload_to='images/products' , null=True , blank=True)
    price = models.IntegerField()
    short_des = models.CharField(max_length=360, null=True)
    description = models.TextField(verbose_name="description", db_index=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, editable=True, blank=True, unique=True)
    is_delete = models.BooleanField(verbose_name='deleted/undelete')

    def get_absolute_url(self):
        return reverse("product-details", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class ProductTag(models.Model):
    tag = models.CharField(max_length=50, verbose_name='TAGS', db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    def __str__(self):
        return f"{self.tag}"

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = 'Tags-List'
