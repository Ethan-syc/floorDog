from django.db import models


# Create your models here.

class MenClothes(models.Model):
    mcid = models.IntegerField(primary_key=True)
    item_url = models.CharField(max_length=500)
    clothes_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=5)
    category = models.CharField(max_length=50)
    pic_url = models.CharField(max_length=500)
    clothes_detail = models.CharField(max_length=500)
    material = models.CharField(max_length=500)
    accessory1 = models.CharField(max_length=500, default='')
    accessory2 = models.CharField(max_length=500, default='')
    accessory3 = models.CharField(max_length=500, default='')
    accessory4 = models.CharField(max_length=500, default='')
    accessory5 = models.CharField(max_length=500, default='')
    accessory6 = models.CharField(max_length=500, default='')
    accessory7 = models.CharField(max_length=500, default='')
    accessory8 = models.CharField(max_length=500, default='')
    accessory9 = models.CharField(max_length=500, default='')
    accessory10 = models.CharField(max_length=500, default='')
    accessory11 = models.CharField(max_length=500, default='')
    accessory12 = models.CharField(max_length=500, default='')
    accessory13 = models.CharField(max_length=500, default='')


class WomenClothes(models.Model):
    wcid = models.IntegerField(primary_key=True)
    item_url = models.CharField(max_length=500)
    clothes_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=5)
    category = models.CharField(max_length=50)
    pic_url = models.CharField(max_length=500)
    clothes_detail = models.CharField(max_length=500)
    material = models.CharField(max_length=500)
    accessory1 = models.CharField(max_length=500, default='')
    accessory2 = models.CharField(max_length=500, default='')
    accessory3 = models.CharField(max_length=500, default='')
    accessory4 = models.CharField(max_length=500, default='')
    accessory5 = models.CharField(max_length=500, default='')
    accessory6 = models.CharField(max_length=500, default='')
    accessory7 = models.CharField(max_length=500, default='')
    accessory8 = models.CharField(max_length=500, default='')
    accessory9 = models.CharField(max_length=500, default='')
    accessory10 = models.CharField(max_length=500, default='')


class MenColor(models.Model):
    id = models.OneToOneField(MenClothes, on_delete=models.CASCADE, primary_key=True)
    color1 = models.CharField(max_length=7, default='')
    color2 = models.CharField(max_length=7, default='')
    color3 = models.CharField(max_length=7, default='')
    color4 = models.CharField(max_length=7, default='')
    color5 = models.CharField(max_length=7, default='')
    color6 = models.CharField(max_length=7, default='')
    color7 = models.CharField(max_length=7, default='')
    color8 = models.CharField(max_length=7, default='')


class WomenColor(models.Model):
    id = models.OneToOneField(WomenClothes, on_delete=models.CASCADE, primary_key=True)
    color1 = models.CharField(max_length=7, default='')
    color2 = models.CharField(max_length=7, default='')
    color3 = models.CharField(max_length=7, default='')
    color4 = models.CharField(max_length=7, default='')
    color5 = models.CharField(max_length=7, default='')
    color6 = models.CharField(max_length=7, default='')
    color7 = models.CharField(max_length=7, default='')
    color8 = models.CharField(max_length=7, default='')

def __str__(self):
    return (
            "item url is" + self.item_url + "\n" + "clothes name is" + self.clothes_name
    )