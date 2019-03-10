from django.db import models

# Create your models here.
class Produto(models.Model):
    nome=models.CharField(max_length=100)
    dt_criacao=models.DateTimeField()
    descricao=models.CharField(max_length=1000)
    valor=models.DecimalField(max_digits=7,decimal_places=2)

    # ao referir ao plural
    class Meta:
        verbose_name_plural='Produtos'

    # ao selecionar, retorna
    def __str__(self):
        return self.nome
