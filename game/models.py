from django.db import models


class JobClass(models.Model):
    name = models.CharField(max_length=32, verbose_name="이름")


class EquipmentClass(models.Model):
    name = models.CharField(max_length=32, verbose_name="이름")
    price = models.PositiveSmallIntegerField(verbose_name="가격")
    defence = models.PositiveSmallIntegerField(verbose_name="방어점")

