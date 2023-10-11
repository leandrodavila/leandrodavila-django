from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid

# Create your models here.

# ----- Empregado -----
class Empregado(models.Model):

    class TipoSalario(models.IntegerChoices):
        HOR = 1, 'Por hora'
        DIA = 2, 'Por dia'
        SEM = 3, 'Por semana'
        QUI = 4, 'Por quinzena'
        MES = 5, 'Por mês'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identificador do Empregado')
    matricula = models.CharField(max_length=30, blank=False)
    nome = models.CharField(max_length=100, blank=False)

    data_admissao   = models.DateField(null=False, blank=False)
    data_deslig     = models.DateField(null=True, blank=True)
    salario         = models.DecimalField(max_digits=9, decimal_places=2)
    unidade_salario = models.PositiveSmallIntegerField(
                        choices=TipoSalario.choices,
                        default=TipoSalario.MES 
                    )
    qtd_horas_semana = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['matricula']

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('empregado-detail', args=[str(self.id)])    
    
    def __str__(self):
        """String for representing the Model object."""
        return f'({self.id}) - {self.matricula}: {self.nome})'

