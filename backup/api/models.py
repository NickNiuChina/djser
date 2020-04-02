from django.db import models

# Create your models here.
class UnitInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    pcid = models.CharField(unique=True, max_length=10)
    order = models.CharField(unique=True, max_length=10)
    customer = models.CharField(max_length=100, blank=True, null=True)
    all_mac = models.CharField(max_length=200)
    ipmi_mac = models.CharField(max_length=45, blank=True, null=True)
    workstation = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit_info'
