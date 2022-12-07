from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
