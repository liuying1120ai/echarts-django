from django.db import models

# Create your models here.


class LineCharts(models.Model):
    xtime = models.TimeField('linetime', null=False)
    value = models.IntegerField('linevalue', null=False)

    class Meta:
        db_table = 'linecharts'

