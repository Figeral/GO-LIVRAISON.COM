from django.db import models
from PIL import Image
from django.utils import timezone
from django.core.validators import MaxValueValidator



#convention:pour les noms des relations c'est du parent aux enfants 


class Category(models.Model):
    status_choice=(
        ('a','Available'),
        ('ua','Unavailable')
    )
    
    reference=models.CharField(max_length=50)
    slug = models.SlugField(default="")
    added=models.DateField("date",auto_now_add=True)
    status = models.CharField(max_length=15,choices=status_choice,default="a")

    def __str__(self):
        return self.reference

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering=['reference']
        
class Supplier(models.Model):
    name=models.CharField(max_length=50)
    category=models.ManyToManyField(Category,related_name='category_supplier')
    store=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    telephone=models.BigIntegerField("+237")
    
    def __str__(self) :
        return self.name
    class Meta:
        db_table = 'supplier'
        managed = True
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'
        ordering=['name']



class Article(models.Model):
    
    status_choice=(
        ('a','Available'),
        ('ua','Unavailable')
    )
    name = models.CharField(max_length=50,null=False,blank=False)
    marque = models.CharField(max_length=50,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="category_article")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,related_name="supplier_article",default=False)
    number=models.BigIntegerField(blank=False,null=False)
    image = models.ImageField(default=False,upload_to='image')
    color=models.CharField(max_length=15)
    # size = models.CharField(max_length=10,null=True,blank=True,default="")
    price = models.BigIntegerField('FCFA')
    added=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15,choices=status_choice,default="a")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'article'
        managed = True
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        ordering=['-added']
        
    @property  
    def number_check(self):
        if self.number< self.Category.quantity:
            return print('the quantity exceeded the amount in warehouse')

def resize(image_path,new_width,new_heigth):
        image=Image.open(image_path)
        image.thumbnail((new_width,new_heigth),image.ANTIALAS)
        return image.save(image_path)


    
