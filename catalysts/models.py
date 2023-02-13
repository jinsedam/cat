from django.db import models
from common.models import CommonModel
from prec_Au_PEG.models import Info as Au_PEG
# Create your models here.

class Catalyst(CommonModel):

    date = models.DateField(null=True, blank=True)
    sample_name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    Au_PEG = models.ManyToManyField(Au_PEG, blank=True, related_name='Catalysts')
    start_temperature = models.FloatField(null=True, blank=True)
    end_temperature = models.FloatField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Catalyst'
        verbose_name_plural = 'Catalyst_Set'
        #ordering = ['sample_name']


        