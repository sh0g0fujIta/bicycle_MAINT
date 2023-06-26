from django.db import models
from .forms import BicycleBrandForm

# Create your models here.

class Toppage(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images/', verbose_name='トップ画像')
    
    def __str__(self):
        return self.title


class Color(models.Model):
    color = models.CharField('色', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.color
    
class Bicycle(models.Model):
    image = models.ImageField(upload_to='images/bycycle/', verbose_name='登録する自転車の画像')
    brand = models.CharField('ブランド', max_length=100, choices=BicycleBrandForm.Brand_Choices)
    model = models.CharField('モデル', max_length=100, null=True, blank=True)
    year = models.CharField('年式', max_length=100, null=True, blank=True)
    update_at = models.DateTimeField('更新日時',null=False, blank=False, auto_now=True)
    
    def __str__(self):
        return self.brand + "_" + self.model + "_" + self.year
    
class Part(models.Model):
    name = models.CharField('パーツ名', max_length=100, null=True, blank=True)
    brand = models.CharField('ブランド', max_length=100, null=True, blank=True)
    type = models.CharField('タイプ', max_length=100, null=True, blank=True)
    price = models.CharField('値段', max_length=100, null=True, blank=True)
    last_inspection_date = models.CharField('最後の点検日付（交換日）', max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name + self.brand
