from __future__ import unicode_literals
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):

    POR_INICIAR = 1
    INICIADA = 2
    EN_PROGRESO = 3
    RETRASADA = 4
    RESUELTA = 5

    STATUS = (
        (POR_INICIAR, 'Por iniciar'),
        (INICIADA, 'Iniciada'),
        (EN_PROGRESO, 'En progreso'),
        (RETRASADA, 'Retrasada'),
        (RESUELTA, 'Resuelta'),
    )

    descripcion = models.CharField(max_length=255)
    fecha_culminacion = models.DateTimeField(null=True)
    user = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS, default=INICIADA)
