from django.db import models
from common.models import CommonModel
from prec_Au.models import Info as Au
from prec_PEG.models import Info as PEG

# Create your models here.

class Info(CommonModel):

    date = models.DateField(null=True, blank=True)
    sample_name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    Au = models.ManyToManyField(Au, related_name='Au_PEG', blank=True)
    PEG = models.ManyToManyField(PEG, related_name='Au_PEG', blank=True)
    Au_input_amount = models.FloatField(null=True, blank=True)
    PEG_input_amount = models.FloatField(null=True, blank=True)
    THF_input_amount = models.FloatField(null=True, blank=True)
    taget_output_amount = models.FloatField(null=True, blank=True)
    real_output_amount = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Information'
        verbose_name_plural = 'Information'
        #ordering = ['sample_name']

    def __str__(self):
        return str(self.sample_name)