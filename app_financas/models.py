from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class SaldosFaturas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saldo_bradesco = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_itau = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_inter = models.DecimalField(max_digits=10, decimal_places=2)
    fatura_bradesco = models.DecimalField(max_digits=10, decimal_places=2)
    fatura_itau = models.DecimalField(max_digits=10, decimal_places=2)
    fatura_inter = models.DecimalField(max_digits=10, decimal_places=2)
    data_atualizacao = models.DateTimeField(auto_now=True)

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]
    data = models.DateField(default=timezone.now)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES, default='saida')
    descricao = models.CharField(max_length=200, default='Sem descrição')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        order_with_respect_to = 'categoria'

    def __str__(self):
        return f"{self.data} - {self.descricao}: R${self.valor}"