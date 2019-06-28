from django.db import models

# Create your models here.
class Bolo(models.Model):
    sabores_opcoes = [
        ('ch','chocolate'),
        ('mr','morango'),
        ('pr','prestigio'),
        ('bl', 'baunilha'),
        ('nh', 'ninho'),
        ('cr', 'churros')
    ]
    recheios_opcoes = [
        ('br', 'brigadeiro'),
        ('dl', 'doce de leite'),
        ('fv', 'frutas vermelas'),
        ('nt', 'nutella'),
        ('bj', 'beijinho'),
        ('nh','ninho'),
        ('sc', 'sem cobertura')
    ]
    coberturas_opcoes = [
        ('gr', 'granulado'),
        ('ct', 'chantilly'),
        ('mr', 'morango'),
    ]
    sabor = models.CharField(max_length=2, choices=sabores_opcoes)
    recheios =  models.CharField(max_length=2, choices=recheios_opcoes)
    coberturas = models.CharField(max_length=2, choices=coberturas_opcoes,default='sc')
    peso = models.DecimalField(decimal_places=2, max_digits=3, default=100.00)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    pagamento_opcoes = [
        ('av','pagamento avista'),
        ('p2', 'pagamento em 2 vezes'),
        ('p3', 'parcelando em 3 vezes')
    ]

    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    cartao = models.IntegerField()
    pagamento = models.CharField(max_length=2, choices=pagamento_opcoes, default='av')


    


