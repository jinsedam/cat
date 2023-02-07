from django.db import models
from common.models import CommonModel
from catalysts.models import Catalyst
# Create your models here.


class ICP_OES(CommonModel):

    class Meta:
        verbose_name = 'ICP_OES'
        verbose_name_plural = 'ICP_OES_Data'
        #ordering = ['sample_name']

class GC(CommonModel):

    which_sample = models.ForeignKey(Catalyst, on_delete=models.PROTECT, related_name='GC')
    request_date = models.DateField()
    completed_date = models.DateField()
    CO_conversion = models.FloatField()

    class Meta:
        verbose_name = 'GC'
        verbose_name_plural = 'GC_Data'
        #ordering = ['sample_name']

class BET(CommonModel):

    which_semple = models.TextField()

    class Meta:
        verbose_name = 'BET'
        verbose_name_plural = 'BET_Data'
        #ordering = ['sample_name']

class TEM(CommonModel):

    date = models.DateField()
    which_sample = models.TextField()

    class Meta:
        verbose_name = 'TEM'
        verbose_name_plural = 'TEM_Data'
        #ordering = ['sample_name']

class TGA(CommonModel):

    date = models.DateField()
    which_Au_PEG = models.ForeignKey()
    Au_content = models.FloatField()

    class Meta:
        verbose_name = 'TGA'
        verbose_name_plural = 'TGA_Data'
        #ordering = ['sample_name']

class SAXS(CommonModel):

    class Meta:
        verbose_name = 'SAXS'
        verbose_name_plural = 'SAXS_Data'
        #ordering = ['sample_name']
