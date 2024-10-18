from django.db import models

# Create your models here.
class emp(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(null=False, max_length=50)
    esalary=models.IntegerField()
    eaddress=models.CharField(null=False, max_length=50)
    econtact=models.BigIntegerField()
