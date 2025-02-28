from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    size = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-time_create"]
        indexes = [
            models.Index(fields=["-time_create"])
        ]
    