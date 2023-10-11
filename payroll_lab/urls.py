from django.urls import path
from . import views as pay_views
from payroll_lab.views import PayrollLabView, InssView, IrrfView, NewEmployeeView, CalcInssView, CalcIrrfView, EmpregadoListView, EmpregadoDetailView

urlpatterns = [
    #path('', pay_views.payroll_lab, name='payroll_lab'),
    #path('payroll_lab/', pay_views.payroll_lab, name='payroll_lab'),

    path('', PayrollLabView.as_view(), name='payroll_lab'),
    path('payroll_lab/', PayrollLabView.as_view(), name='payroll_lab'),

    path('inss/', InssView.as_view(), name='inss'),
    path('irrf/', IrrfView.as_view(), name='irrf'),

    #path('cad_ee/', NewEmployeeView.as_view(), name='cad_ee'),
    path('cad_ee/', EmpregadoListView.as_view(), name='cad_ee'),
    path('empregado-detail/<uuid:pk>', EmpregadoDetailView.as_view(), name='empregado-detail'),
    path('calc_inss/', CalcInssView.as_view(), name='calc_inss'),
    path('calc_irrf/', CalcIrrfView.as_view(), name='calc_irrf')
]
