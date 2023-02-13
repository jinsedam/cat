from django.db import models
from common.models import CommonModel
# Create your models here.

class Info(CommonModel):

    date = models.DateField(null=True, blank=True)
    sample_name = models.CharField(max_length=50, null=True, blank=True, unique=True)
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
        verbose_name = 'Information'
        verbose_name_plural = 'Information'
        #ordering = ['sample_name']

    def __str__(self):
        return str(self.sample_name)