from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        verbose_name='Category name',
        max_length=50,
        db_index=True
    )
    slug = models.SlugField(
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        verbose_name='Product category',
        on_delete=models.CASCADE,
        related_name='product_category'
    )
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Price for a piece'
    )
    product_name = models.CharField(
        verbose_name='Product name',
        max_length=50
    )
    product_description = models.TextField(
        verbose_name='Description',
    )
    composition = models.TextField(
        verbose_name='Composition',
    )
    is_new = models.BooleanField(
        verbose_name='Is this product new',
        default=True
    )
    is_active = models.BooleanField(
        verbose_name='Is this product currently active',
        default=True
    )
    created = models.DateTimeField(
        verbose_name='A creation date',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='Updated',
        auto_now=True
    )

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.product_name


class Images(models.Model):
    image_name = models.CharField(
        verbose_name='Image name',
        max_length=50
    )
    slug = models.SlugField(
        max_length=50,
        unique=True
    )
    image = models.ImageField(
        upload_to='images/'
    )
