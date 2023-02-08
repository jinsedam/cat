from django.db import models
from common.models import CommonModel
from catalysts.models import Catalyst
from precursors.models import Au_PEG
# Create your models here.


class ICP_OES(CommonModel):

    class Meta:
        verbose_name = 'ICP_OES'
        verbose_name_plural = 'ICP_OES_Data'
        #ordering = ['sample_name']

class GC(CommonModel):

    which_catalyst = models.ForeignKey(Catalyst, on_delete=models.PROTECT, related_name='GC', null=True, blank=True)
    request_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)
    CO_conversion = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'GC'
        verbose_name_plural = 'GC_Data'
        #ordering = ['sample_name']

class BET(CommonModel):

    which_catalyst = models.ForeignKey(Catalyst, on_delete=models.PROTECT, related_name='BET', null=True, blank=True)
    request_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)
    BET_surface_area = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'BET'
        verbose_name_plural = 'BET_Data'
        #ordering = ['sample_name']

class TEM(CommonModel):

    which_catalyst = models.ForeignKey(Catalyst, on_delete=models.PROTECT, related_name='TEM', null=True, blank=True)
    request_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'TEM'
        verbose_name_plural = 'TEM_Data'
        #ordering = ['sample_name']

class TGA(CommonModel):

    which_Au_PEG = models.ForeignKey(Au_PEG, on_delete=models.PROTECT, related_name='TGA', null=True, blank=True)
    request_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)
    Au_content = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'TGA'
        verbose_name_plural = 'TGA_Data'
        #ordering = ['sample_name']

class SAXS(CommonModel):

    class Meta:
        verbose_name = 'SAXS'
        verbose_name_plural = 'SAXS_Data'
        #ordering = ['sample_name']
