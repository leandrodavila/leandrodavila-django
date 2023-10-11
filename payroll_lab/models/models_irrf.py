from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid

# Create your models here.
class IrrfRange(models.Model):

    #id = models.IntegerField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identificador da faixa da Tabela do IRRF')
    #tableId = models.ForeignKey('InssTable', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=50, blank=True)
    low_amount = models.DecimalField(max_digits=9, decimal_places=2)
    high_amount = models.DecimalField(max_digits=9, decimal_places=2)
    deduction_amount = models.DecimalField(max_digits=7, decimal_places=2)
    rate = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['low_amount']

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('irrf-range-detail', args=[str(self.id)])    
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.description} - ({self.low_amount}) - ({self.high_amount}) - ({self.rate}%)'

# ----- IRRF -----    
class IrrfTable(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identificador da Tabela de IRRF')
    description = models.CharField(max_length=100)
    valid_from = models.DateField(null=False, blank=False)
    simplified_deduction = models.DecimalField(max_digits=7, decimal_places=2)
    dependent_deduction = models.DecimalField(max_digits=7, decimal_places=2)
    irrf_ranges = models.ManyToManyField(IrrfRange, verbose_name='irrf_ranges')

    class Meta:
        ordering = ['-valid_from']

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('irrf-table-detail', args=[str(self.id)])    
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.description} Válido desde: ({self.valid_from})'

    