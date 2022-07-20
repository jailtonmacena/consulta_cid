from django.db import models


class DoencaCategoria(models.Model):
    """Definindo categoria e descricao de uma doença com CID10"""
    categoria = models.CharField(max_length=4)
    descricao = models.TextField()


    def __str__(self):
        """Retornar uma representação em string do atributo categoria"""
        return self.categoria


class DoencaGrupo(models.Model):
    """Definindo categoriainicial e final para os grupos de doença com CID10"""
    categoria_inicial = models.CharField(max_length=4)
    categoria_final = models.CharField(max_length=4)
    descricao = models.TextField()


    def __str__(self):
        """Retorna uma representação em string do atributo categoria_inicial"""
        return self.categoria_inicial
