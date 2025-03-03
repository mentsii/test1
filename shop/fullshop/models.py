from django.db import models
from django.urls import reverse

class ActiveProductsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=Product.Status.Active)

class Product(models.Model):
    class Status(models.IntegerChoices): 
        Inactive = 0, "Товар в продаже"
        Active = 1, "Товар не в продаже"

    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    size = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(choices=Status.choices, default=Status.Active)
    price = models.IntegerField(default=2000)
    count = models.IntegerField(default=10)
    cate = models.ForeignKey('Category', on_delete=models.PROTECT, related_name="products")

    active_products = ActiveProductsManager()
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-time_create"]
        indexes = [
            models.Index(fields=["-time_create"])
        ]

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse("category", kwargs={"cate_slug": self.slug})

    def __str__(self):
        return self.title
    