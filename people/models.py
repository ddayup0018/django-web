from django.db import models

class People(models.Model):
    xm = models.CharField(max_length=8)
    sfzh = models.CharField(max_length=32)
    sjhm = models.CharField(max_length=16)
    xb = models.CharField(max_length=2)
    nl = models.CharField(max_length=2)
    zw = models.CharField(max_length=8)
    gj = models.CharField(max_length=8)
    nsr = models.CharField(max_length=16)
    xl = models.CharField(max_length=8)
    hyzk = models.CharField(max_length=4)
    zzmm = models.CharField(max_length=8)
    hjxx = models.CharField(max_length=255)
    tc = models.CharField(max_length=255)

    # def __unicode__(self):
    #     return self.objects

    class Meta:
        db_table='people_table'