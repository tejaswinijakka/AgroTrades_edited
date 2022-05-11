from django.db import models
from .category import Category
class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    phoneno = models.CharField(max_length=10, default='9876543210')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='Price Per kg', blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids)

    @staticmethod
    def get_all_products():
        return Products.objects.all()


    @staticmethod
    def get_all_products_by_category_id(category_id):
        if (category_id):
            return Products.objects.filter(category=category_id)
        else:
            return Products.objects.all()