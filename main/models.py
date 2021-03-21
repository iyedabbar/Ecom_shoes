from django.db import models
from django.utils.html import mark_safe
class Banner(models.Model):
    img = models.ImageField(upload_to="img/")
    alt_text = models.CharField(max_length=3200)

    class Meta:
        verbose_name_plural= '1. Banners '


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/") 

    class Meta:
        verbose_name_plural= '2. Categories'
    
    def Category_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))


    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/") 
    
    def Brand_image(self):
        return mark_safe('<img src="%s" width="70" height="50"/>' % (self.image.url))
    
    class Meta:
        verbose_name_plural= '3. Brands'

    def __str__(self):
        return self.title 


class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def Color_bg(self):
        return mark_safe('<div style= "width:50px ;  height:50px ; background:%s"></div>' % (self.color_code))

    class Meta:
        verbose_name_plural= '4. Colors'

    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural= '5. Sizes'
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="prod_img/") 
    slug = models.CharField(max_length=400)
    detail = models.TextField()
    specs = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=True)
 
    class Meta:
        verbose_name_plural= '6. Products'
    
    def Product_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))

    def __str__(self):
        return self.title

class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    
    
    class Meta:
        verbose_name_plural= '7. ProductAttributes'

    def __str__(self):
        return self.product.title