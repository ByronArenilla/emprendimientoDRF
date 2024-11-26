from django.db import models
from django.utils.translation import gettext_lazy as _

class RoleChoices(models.TextChoices):
    ADMINISTRADOR = 'ADMIN', _('Administrador')
    USUARIO = 'USER', _('Usuario')

class Roles(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(
        max_length=5,  # Tamaño del valor más largo
        choices=RoleChoices.choices,
        default=RoleChoices.USUARIO,
    )
