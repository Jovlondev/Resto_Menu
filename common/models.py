from django.db import models
from .auth_models import User


# Create your models here.
class Category(models.Model):
    type_choices = [
        ("fast-food", "Fast-food"),
        ("an'anaviy", "An'anaviy"),
        ("yengil", "Yengil taomlar"),
        ("ichimlik", "Ichimliklar"),
        ("shirinlik", "Shirinliklar"),
        ("turkish","Turkiya Taomlari")
    ]
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128,choices=type_choices)

    def __str__(self):
        return f"{self.name}"

    def get_type(self):
        return dict(self.type_choices)[self.type]

class Meal(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    skidka = models.SmallIntegerField(default=0,verbose_name="Chegirma(%)")
    ctg = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='ovqat')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name}"
    def org_price(self):
        if self.skidka:
            narx = self.price * (1-self.skidka/100)
            return f'{int(narx):,}'
        return f'{self.price:,}'
    def first_image(self):
        if self.images.first():
            return self.images.first().image


class OvqatImg(models.Model):
    meals = models.ForeignKey(Meal,on_delete = models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='meal/')