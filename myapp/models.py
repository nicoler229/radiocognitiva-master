

from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),) 


class ConexionActual(models.Model):
    
    rec_id = models.IntegerField(primary_key=True)
    frecuencia = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    tx_id = models.CharField(max_length=50, blank=True, null=True)
    rx_id = models.CharField(max_length=50, blank=True, null=True)
    bw = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'conexion_actual'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'django_session'


class HistorialSesiones(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    conexion_id = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'historial_sesiones'


class ParametrosIniciales(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    frecuencia_inicial = models.CharField(max_length=50, blank=True, null=True)
    frecuencia_final = models.CharField(max_length=50, blank=True, null=True)
    bw = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'parametros_iniciales'


class Receptor(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    frecuencia = models.CharField(max_length=50, blank=True, null=True)
    dispositivo = models.CharField(max_length=50, blank=True, null=True)
    fecha_conexion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'receptor'


class Transmisor(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    frecuencia = models.CharField(max_length=50, blank=True, null=True)
    dispositivo = models.CharField(max_length=50, blank=True, null=True)
    fecha_conexion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'myapp'
        managed = False
        db_table = 'transmisor'
        
class Canales(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    frecuencia = models.FloatField() 
    bandwidth = models.FloatField()  
    potencia = models.FloatField()     
    
class Archivos(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True) 
    archivo_mp3 = models.FileField(upload_to='canciones/')
    ancho_de_banda_requerido = models.FloatField()  