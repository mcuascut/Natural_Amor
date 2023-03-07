from django.db import models
    
class Category(models.Model):
    
    title = models.CharField(max_length=50)
    
    class Meta: 
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)    
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

        
    
    
