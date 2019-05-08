# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Title(models.Model):
    id = models.BigAutoField(primary_key=True)
    scraping_date = models.DateField()
    url = models.CharField(max_length=100)
    title_name = models.CharField(max_length=50)
    title_type = models.CharField(max_length=50)
    interest = models.DecimalField(max_digits=14, decimal_places=4)
    interest_type = models.CharField(max_length=50)
    title_value = models.DecimalField(max_digits=14, decimal_places=4)
    minimum_value = models.DecimalField(max_digits=14, decimal_places=4)
    liquidity = models.IntegerField()
    total_time = models.IntegerField()
    ending_date = models.DateField()
    emitter = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    emitter_risk_level = models.IntegerField()
    emitter_risk_level_type = models.CharField(max_length=50)
    fgc = models.IntegerField()
    ir = models.IntegerField()

    def __str__(self):
        return str(self.title_name)

    class Meta:
        db_table = 'title'


