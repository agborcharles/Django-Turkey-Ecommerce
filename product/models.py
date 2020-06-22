from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    STATUS = (
        ("True", "True"),
        ("False", "False"),

    )

    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.CharField(max_length=200, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

# Get the you want the model to display in the Dashboard
    def __str__(self):
        return self.title

# Auto Save Title of the Item to the Slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    STATUS = (
        ("True", "True"),
        ("False", "False"),

    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    minamount = models.IntegerField()
    details = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.CharField(max_length=200, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

# Get the you want the model to display in the Dashboard
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

# Return the name of the Object Created
    def __str__(self):
        return self.title

# Auto Save Title of the Item to the Slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
