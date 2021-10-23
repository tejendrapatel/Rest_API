from django.db import models
class contactss(models.Model):
    name = models.CharField(max_length=30,null=True)
    subject = models.CharField(max_length=30,null=True,blank=False)
    Email = models.EmailField(null=True)
    Address = models.TextField(null=True)
