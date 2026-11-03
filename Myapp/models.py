from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.category_name

class Products(models.Model):
    categorys=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()

    def __str__(self):
        return self.product_name