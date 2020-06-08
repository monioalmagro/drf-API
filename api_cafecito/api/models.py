from django.db import models

class Producto(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    
    image = models.ImageField()
    description = models.TextField(help_text="Descripción del producto")
    stock = models.BooleanField(default=False)
    
    

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']
       

    def __str__(self):
        return self.name

    