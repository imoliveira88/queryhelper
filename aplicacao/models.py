from django.db import models

class Sistema(models.Model):
    nome = models.CharField('Nome', unique=True, max_length=20, blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'
        ordering = ['nome']

class Modulo(models.Model):
    nome = models.CharField('Nome', unique=True, max_length=20, blank=False)
    sistema = models.ForeignKey(Sistema, verbose_name='Sistema',  db_column='sistema_id',  on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulo'
        ordering = ['nome']

class Query(models.Model):
    nome = models.CharField('Nome', unique=True, max_length=100, blank=False)
    descricao = models.CharField('Descricao', unique=False, max_length=200, blank=False, default="Descrição padrão")
    sistema = models.ForeignKey(Sistema, verbose_name='Sistema',  db_column='sistema_id',  on_delete=models.PROTECT, blank=False, null=False)
    modulo = models.ForeignKey(Modulo, verbose_name='Modulo',  db_column='modulo_id',  on_delete=models.PROTECT, blank=True, null=True)
    query = models.CharField('Query', unique=True, max_length=5000, blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'
        ordering = ['nome']
