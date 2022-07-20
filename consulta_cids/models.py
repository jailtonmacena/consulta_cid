from django.db import models


class Doencacategoria(models.Model):
    """Definindo categoria e descricao de uma doença com CID10"""
    categoria = models.CharField(max_length=4)
    descricao = models.TextField()
