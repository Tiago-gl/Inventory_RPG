from django.db import models
from django.contrib.auth.models import User

class Classe(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    atributos = models.JSONField()  # Exemplo de uso para armazenar atributos

    def __str__(self):
        return self.nome

class Raca(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    atributos = models.JSONField()  # Exemplo de uso para armazenar atributos

    def __str__(self):
        return self.nome

class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    nivel = models.PositiveIntegerField(default=1)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.usuario.username})"
