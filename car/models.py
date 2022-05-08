from django.db import models

class Car(models.Model):
    cym = models.CharField(max_length=16,unique=True)
    cphm = models.CharField(max_length=16)
    xszzb = models.ImageField(upload_to='car/pictures')
    xszfb = models.ImageField(upload_to='car/pictures')
    cldjsj = models.CharField(max_length=32)
    clgls = models.CharField(max_length=32)
    clzk = models.CharField(max_length=32)
    pcqk = models.CharField(max_length=16)


    def __str__(self):
        return self.cym

    class Meta:
        db_table='car_table'

class Car_anpai(models.Model):
    cym = models.CharField(max_length=16)
    jsy = models.CharField(max_length=16)
    ycsy = models.CharField(max_length=128)
    pcsj = models.DateTimeField(auto_now_add=True)
    ghsj = models.DateTimeField(auto_now=True)
    csyf = models.CharField(max_length=16)
    csgls = models.CharField(max_length=16)
    syclzk = models.CharField(max_length=32)
    pcqk = models.CharField(max_length=16)

    def __str__(self):
        return self.cym

    class Meta:
        db_table='car_anpai_table'