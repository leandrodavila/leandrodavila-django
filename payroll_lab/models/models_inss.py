from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid

# Create your models here.

# ----- INSS -----
class InssRange(models.Model):

    #id = models.IntegerField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identificador do range da Tabela do INSS')
    #tableId = models.ForeignKey('InssTable', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=50, blank=True)
    low_amount = models.DecimalField(max_digits=7, decimal_places=2)
    high_amount = models.DecimalField(max_digits=7, decimal_places=2)
    rate = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['low_amount']

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('inss-range-detail', args=[str(self.id)])    
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.description} - ({self.low_amount}) - ({self.high_amount}) - ({self.rate}%)'


class InssTable(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identificador da Tabela do INSS')
    description = models.CharField(max_length=100)
    valid_from = models.DateField(null=False, blank=False)
    inss_ranges = models.ManyToManyField(InssRange, verbose_name='inss_ranges')

    class Meta:
        ordering = ['-valid_from']

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('inss-table-detail', args=[str(self.id)])    
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.description} Válido desde: ({self.valid_from})'
    
    