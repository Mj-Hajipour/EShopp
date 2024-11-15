from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length=150,verbose_name="عنوان")
    name=models.CharField(max_length=150,verbose_name='عنوان جستجو')

    class Meta:
         verbose_name='دسته بندی محصولات'
         verbose_name_plural='دسته بندی محصولات'
    def __str__(self):
        return self.title