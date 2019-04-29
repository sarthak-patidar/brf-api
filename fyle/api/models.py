from django.db import models

# Create your models here.


class Branch(models.Model):
    ifsc = models.CharField(max_length=15, null=False)
    bank_id = models.IntegerField(null=False)
    branch = models.CharField(max_length=150, null=False)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=100, null=False)
    district = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=200, null=False)
    bank_name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return "{} - {}".format(self.bank_name, self.branch)
