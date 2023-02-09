from django.db import models
from common.models import CommonModel
# Create your models here.

class Au(CommonModel):

    date = models.DateField(null=True, blank=True)
    sample_name = models.CharField(max_length=50, null=True, blank=True)
    HAuCl4_input_amount = models.FloatField(null=True, blank=True)
    Toluene_input_amount = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Au'
        verbose_name_plural = 'Au_Set'
        #ordering = ['sample_name']

class PEG(CommonModel):

    date = models.DateField(null=True, blank=True)
    sample_name = models.CharField(max_length=50, null=True, blank=True)
    MPEG_input_amount = models.FloatField(null=True, blank=True)
    TGA_input_amount = models.FloatField(null=True, blank=True)
    Toluene_input_amount = models.FloatField(null=True, blank=True)
    operating_temperature = models.FloatField(null=True, blank=True)
    operating_RPM = models.FloatField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    duration_time = models.TimeField(null=True, blank=True)
    taget_amount = models.FloatField(null=True, blank=True)
    real_output_amount = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'PEG'
        verbose_name_plural = 'PEG_Set'
        #ordering = ['sample_name']

class Au_PEG(CommonModel):

    date = models.DateField(null=True, blank=True)
    sample_name = models.CharField(max_length=50, null=True, blank=True)
    Au = models.ForeignKey(Au, on_delete=models.PROTECT, related_name='Au_PEG', null=True, blank=True)
    PEG = models.ForeignKey(PEG, on_delete=models.PROTECT, related_name='Au_PEG', null=True, blank=True)
    Au_input_amount = models.FloatField(null=True, blank=True)
    PEG_input_amount = models.FloatField(null=True, blank=True)
    THF_input_amount = models.FloatField(null=True, blank=True)
    taget_output_amount = models.FloatField(null=True, blank=True)
    real_output_amount = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Au_PEG'
        verbose_name_plural = 'Au_PEG_Set'
        #ordering = ['sample_name']