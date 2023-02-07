from django.db import models
from common.models import CommonModel
# Create your models here.

class Catalyst(CommonModel):

    date = models.DateField()
    sample_name = models.TextField(max_length=50)
    which_Au_PEG = models.ForeignKey()
    target_Au_content = models.FloatField()
    start_temperature = models.FloatField()
    end_temperature = models.FloatField()
    
    class Meta:
        verbose_name = 'Catalyst'
        verbose_name_plural = 'Catalyst_Set'
        #ordering = ['sample_name']


        