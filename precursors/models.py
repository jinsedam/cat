from django.db import models
from common.models import CommonModel
# Create your models here.

class Au(CommonModel):

    date = models.DateField()
    sample_name = models.TextField(max_length=50)
    HAuCl4_input_amount = models.FloatField()
    Toluene_input_amount = models.FloatField()

    class Meta:
        verbose_name = 'Au'
        verbose_name_plural = 'Au_Set'
        #ordering = ['sample_name']

class PEG(CommonModel):

    date = models.DateField()
    sample_name = models.TextField(max_length=50)
    input_amount_MPEG = models.FloatField()
    input_amount_TGA = models.FloatField()
    input_amount_Toluene = models.FloatField()
    operating_temperature = models.FloatField()
    operating_RPM = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    taget_amount = models.FloatField()
    real_output_amount = models.FloatField()

    class Meta:
        verbose_name = 'PEG'
        verbose_name_plural = 'PEG_Set'
        #ordering = ['sample_name']

class Au_PEG(CommonModel):

    date = models.DateField()
    sample_name = models.TextField(max_length=50)
    which_Au = models.ForeignKey(Au, on_delete=models.PROTECT, related_name='Au_PEG')
    which_PEG = models.ForeignKey(PEG, on_delete=models.PROTECT, related_name='Au_PEG')
    Au_input_amount = models.FloatField()
    PEG_input_amount = models.FloatField()
    THF_input_amount = models.FloatField()
    taget_output_amount = models.FloatField()
    real_output_amount = models.FloatField()
    Au_content = models.FloatField()

    class Meta:
        verbose_name = 'Au_PEG'
        verbose_name_plural = 'Au_PEG_Set'
        #ordering = ['sample_name']