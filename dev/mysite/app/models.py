from django.db import models

# Create your models here.

class Toppage(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images', verbose_name=' トップ画像')
    
    def __str__(self):
        return self.title