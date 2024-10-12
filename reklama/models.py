from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField( max_length=150)
    class Meta:
        db_table = 'Catagory'
        managed = True
        verbose_name = 'Catagory'
        verbose_name_plural = 'Catagories'
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField( max_length=150)
    slug = models.SlugField(null=False, blank=True,unique=True,db_index=True,editable=False)
    discription = models.TextField()
    price = models.DecimalField( max_digits=10, decimal_places=2)
    surat = models.FileField(upload_to='product_image',default=None,blank=False)
    Category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super().save()  
    def __str__(self):
        return self.name
    
    