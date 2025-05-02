from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=256)
    sobrenome = models.CharField(max_length=256, blank=True, null=True)
    endereco = models.CharField(max_length=256)
    telefone = models.CharField(max_length=35)
    email = models.EmailField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.nome + " " + self.sobrenome