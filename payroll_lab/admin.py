from django.contrib import admin
#from payroll_lab.models import InssTable, InssRange, IrrfTable, IrrfRange

from payroll_lab.models.models_inss import InssTable, InssRange
from payroll_lab.models.models_irrf import IrrfTable, IrrfRange
from payroll_lab.models.models_empregado import Empregado

# Register your models here.
admin.site.register(InssTable)
admin.site.register(InssRange)

admin.site.register(IrrfTable)
admin.site.register(IrrfRange)

admin.site.register(Empregado)

