# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConexionActual(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    frecuencia = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    tx_id = models.CharField(max_length=50, blank=True, null=True)
    rx_id = models.CharField(max_length=50, blank=True, null=True)
    bw = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conexion_actual'


class HistorialSesiones(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    conexion_id = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_sesiones'


class ParametrosIniciales(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    frecuencia_inicial = models.CharField(max_length=50, blank=True, null=True)
    frecuencia_final = models.CharField(max_length=50, blank=True, null=True)
    bw = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametros_iniciales'


class Receptor(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    frecuencia = models.CharField(max_length=50, blank=True, null=True)
    dispositivo = models.CharField(max_length=50, blank=True, null=True)
    fecha_conexion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receptor'


class Transmisor(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    frecuencia = models.CharField(max_length=50, blank=True, null=True)
    dispositivo = models.CharField(max_length=50, blank=True, null=True)
    fecha_conexion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transmisor'
