from django.db import models
from django.contrib.auth.models import User

class Reservoir(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rname=models.CharField(max_length=100)
    targets_number=models.PositiveIntegerField()
    rimage=models.ImageField(blank=True,null=True)
    rregion=models.CharField(max_length=150)
    rdistrict=models.CharField(max_length=150)

    def __str__(self):
        return self.rname

class Target(models.Model):
    t_user=models.ForeignKey(User,on_delete=models.CASCADE)
    target_name=models.CharField(max_length=100)
    k1value=models.PositiveIntegerField()
    k2value=models.PositiveIntegerField()
    k3value=models.PositiveIntegerField() 
    resevoirid=models.ForeignKey(Reservoir,on_delete=models.CASCADE)
    timage=models.ImageField(blank=True, null=True) 

    def __str__(self):
        return self.target_name

class Indicator(models.Model):
    i_user=models.ForeignKey(User,on_delete=models.CASCADE)
    iname=models.CharField(max_length=100)
    parametres=models.CharField(max_length=250)
    targetid=models.ForeignKey(Target,on_delete=models.CASCADE)

    def __str__(self):
        return self.iname

class History(models.Model):
    h_user=models.ForeignKey(User,on_delete=models.CASCADE)
    hreservoirid=models.ForeignKey(Reservoir,on_delete=models.CASCADE)
    htargetid=models.ForeignKey(Target,on_delete=models.CASCADE)
    indicatorid=models.ForeignKey(Indicator,on_delete=models.CASCADE)
    hvalue=models.PositiveIntegerField()


                     
                    