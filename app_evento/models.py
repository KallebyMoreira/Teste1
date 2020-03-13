from django.contrib.auth.models import User
from django.db import models


class Pessoa(models.Model):
    usuario = models.OneToOneField(User,on_delete = models.CASCADE,
        verbose_name = 'Usuário')
    nome = models.CharField("Nome", max_length=128)
    email = models.EmailField('E-mail',null=True,blank=True)
    def __str__(self):
        return self.nome
class Pfisica(Pessoa):
    cpf = models.IntegerField('CPF',max_length=11)
    def __str__(self):
        return self.nome

class Evento(models.Model):
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    nome = models.CharField('Nome',max_length=128, blank=True, null=True)
    sigla = models.CharField('Sigla',max_length=128, blank=True, null=True)
    data_publicacao = models.DateTimeField('Data inicial', blank=True, null=True)
    realizador = models.ForeignKey(Pessoa,on_delete=models.CASCADE,verbose_name='Realizador',max_length=128, blank=True, null=True)
    descricao = models.TextField('Descrição')

    def __str__(self):
        return self.nome


class Ingresso(models.Model):
    descricao = models.CharField("Descrição", max_length=128)
    valor = models.FloatField('Valor')
    evento = models.ForeignKey(Evento,on_delete=models.CASCADE,verbose_name = "Evento", blank = True,null = True)
    def __str__(self):
        return self.descricao

class Inscrição(models.Model):
    pessoa= models.ForeignKey(Pessoa,on_delete=models.CASCADE,verbose_name = "Pessoa", blank = True,null = True)
    evento = models.ForeignKey(Evento,on_delete=models.CASCADE,verbose_name = "Evento", blank = True,null = True)
    ingresso = models.ForeignKey(Ingresso,on_delete=models.CASCADE,verbose_name = "Ingresso", blank = True,null = True)
    def __str__(self):
        return self.evento



