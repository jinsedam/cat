from django.db import models

# Create your models here.
from django.db import models
from common.models import CommonModel
from catalysts.models import Catalyst
from prec_Au_PEG.models import Info as Au_PEG
# Create your models here.

class Data(CommonModel):
    catalyst = models.ForeignKey(Catalyst, on_delete=models.PROTECT, related_name='TEM',null=True, blank=True)
    Au_PEG = models.ForeignKey(Au_PEG, on_delete=models.PROTECT, related_name='TEM',null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Data'
        ordering = ['catalyst', 'Au_PEG']

class Photo(CommonModel):
    figure = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    data = models.ForeignKey(Data, on_delete=models.PROTECT, null=True, blank=True, related_name='photos')
