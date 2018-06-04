# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# class ConvertingDateTimeField(models.DateTimeField):

#     def get_prep_value(self, value):

#         return str(datetime.strptime(str(value), '%Y-%m-%d %H:%M:%S'))

class Admin(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    vezife = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefon = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'admin'


class Ats(models.Model):
    ats = models.CharField(max_length=1500)

    class Meta:
        managed = False
        db_table = 'ats'


class HellOlan(models.Model):
    ivr_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hell_olan'


class Icracilar(models.Model):
    isci_haqqinda = models.ForeignKey('IsciHaqqinda', models.DO_NOTHING)
    erazisi = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'icracilar'


class IcradaOlanlar(models.Model):
    kadr_adi = models.CharField(max_length=50)
    ivr = models.ForeignKey('Ivr', models.DO_NOTHING)
    ats = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icrada_olanlar'


class Idareler(models.Model):
    idare_adi = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'idareler'


class IsciHaqqinda(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    ata_adi = models.CharField(max_length=50)
    doguldugu_tarix = models.CharField(max_length=50)
    unvan = models.CharField(max_length=50)
    vetendasliq = models.CharField(max_length=50)
    herbi = models.CharField(max_length=50)
    isden_cixis_sebebi = models.CharField(max_length=1500)
    sehadetname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefon = models.CharField(max_length=50)
    mobil = models.CharField(max_length=50)
    son_is = models.CharField(max_length=1500)
    is_telefonu = models.CharField(max_length=50)
    daxili_nomre = models.CharField(max_length=50)
    sobe = models.ForeignKey('Sobeler', models.DO_NOTHING)
    vezife = models.ForeignKey('Vezifeler', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'isci_haqqinda'


class IslemeHuquqOlanlar(models.Model):
    istifadeci_adi = models.CharField(primary_key=True, max_length=50)
    sifre = models.CharField(max_length=50)
    isci = models.ForeignKey(IsciHaqqinda, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'isleme_huquq_olanlar'


class Ivr(models.Model):
    
    full_name = models.CharField(max_length=50, blank=True, null=True)
    zeng_eden = models.CharField(max_length=50, blank=True, null=True)
    menbe = models.CharField(max_length=50, blank=True, null=True)
    abonent_kodu = models.CharField(max_length=50, blank=True, null=True)
    sobe = models.ForeignKey('Sobeler', models.DO_NOTHING, blank=True, null=True)
    shikayet_katigoriya = models.CharField(max_length=50, blank=True, null=True)
    xususi_qeyd = models.CharField(max_length=1000, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    tarix = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    hal = models.CharField(max_length=50, blank=True, null=True)
    gonderilen_sexs = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'ivr'


class IvrOld(models.Model):
    full_name = models.CharField(max_length=50, blank=True, null=True)
    zeng_eden = models.CharField(max_length=50, blank=True, null=True)
    menbe = models.CharField(max_length=50, blank=True, null=True)
    abonent_kodu = models.CharField(max_length=50, blank=True, null=True)
    sobe_id = models.IntegerField(blank=True, null=True)
    shikayet_katigoriya = models.CharField(max_length=50, blank=True, null=True)
    xususi_qeyd = models.CharField(max_length=1500, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    tarix = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    hal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivr_old'


class Kadrlar(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    ata_adi = models.CharField(max_length=50)
    vezife = models.ForeignKey('Vezifeler', models.DO_NOTHING)
    email = models.CharField(max_length=50)
    telefon = models.CharField(max_length=50)
    telefon2 = models.CharField(max_length=50)
    daxili_nomre = models.CharField(max_length=50)
    sobe = models.ForeignKey('Sobeler', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'kadrlar'


class Mezuniyyet(models.Model):
    sobe = models.ForeignKey('Sobeler', models.DO_NOTHING)
    vezife = models.ForeignKey('Vezifeler', models.DO_NOTHING)
    mezuniyyet_muddeti = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mezuniyyet'


class ProbleminKodu(models.Model):
    problemin_kodu = models.IntegerField(primary_key=True)
    haqqinda = models.CharField(max_length=1500)

    class Meta:
        managed = False
        db_table = 'problemin_kodu'


class Qalan(models.Model):
    ivr_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qalan'


class Sobeler(models.Model):
    sobe = models.CharField(max_length=50)
    idare = models.ForeignKey(Idareler, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sobeler'


class Vezifeler(models.Model):
    vezife = models.CharField(max_length=50)
    sobe = models.ForeignKey(Sobeler, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vezifeler'


class YeniQosulma(models.Model):
    sifarisci = models.CharField(max_length=50)
    sifarisci_nomre = models.CharField(max_length=50)
    unvan = models.CharField(max_length=50)
    xususi_qeyd = models.CharField(max_length=50)
    sobe = models.ForeignKey(Sobeler, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'yeni_qosulma'