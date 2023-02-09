from django.db import models
from common.models import CommonModel
from catalysts.models import Catalyst

# Create your models here.

class Data(CommonModel):
    catalyst = models.ForeignKey(Catalyst, on_delete=models.PROTECT, related_name='GC',null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    CO_conversion = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Data'
        ordering = ['catalyst']

class Photo(CommonModel):
    figure = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    data = models.ForeignKey(Data, on_delete=models.PROTECT, null=True, blank=True, related_name='photos')

