from django.shortcuts import render
from django.views import View, generic
from home.navigation import SideBarPL, SideBarMixin
from .models import InssTable, IrrfTable
from .models import Empregado

# Create your views here.

class PayrollLabView(View, SideBarMixin):

    def get(self, request):

        my_context = self.get_context_sidebar()

        # Render the HTML template index.html with the data in the context variable
        return render(request, 'payroll_lab/payroll_lab.html', context=my_context)


class InssView(View, SideBarMixin):

    def get(self, request):

        my_context = self.get_context_sidebar(SideBarPL.URL_ID_CONF)

        inss_tables = InssTable.objects.all()
        
        my_context.update( {"inss_tables": inss_tables})
    
        # Render the HTML template index.html with the data in the context variable
        return render(request, 'payroll_lab/inss.html', context=my_context)

class IrrfView(View, SideBarMixin):

    def get(self, request):

        my_context = self.get_context_sidebar(SideBarPL.URL_ID_CONF)
        irrf_tables = IrrfTable.objects.all

        my_context.update({"irrf_tables": irrf_tables})

        # Render the HTML template index.html with the data in the context variable
        return render(request, 'payroll_lab/irrf.html', context=my_context)

class NewEmployeeView(View, SideBarMixin):

    def get(self, request):

        my_context = self.get_context_sidebar(SideBarPL.URL_ID_PLAY)

        # Render the HTML template index.html with the data in the context variable
        return render(request, 'payroll_lab/cad_ee.html', context=my_context)
    
class EmpregadoListView(generic.ListView,  SideBarMixin):

    model = Empregado
    template_name = 'payroll_lab/empregado_list.html'

    def get_context_data(self, **kwargs):

        #Call the base implementation first to get the context
        context = super(EmpregadoListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        my_context =  self.get_context_sidebar(SideBarPL.URL_ID_PLAY)
        context.update(my_context)
        return context
    
class EmpregadoDetailView(generic.DetailView,  SideBarMixin):

    model = Empregado
    template_name = 'payroll_lab/empregado_list.html'

    def get_context_data(self, **kwargs):

        #Call the base implementation first to get the context
        context = super(EmpregadoListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        my_context =  self.get_context_sidebar(SideBarPL.URL_ID_PLAY)
        context.update(my_context)
        return context


class CalcInssView(View, SideBarMixin):

    def get(self, request):

        my_context = self.get_context_sidebar(SideBarPL.URL_ID_PLAY)

        # Render the HTML template index.html with the data in the context variable
        return render(request, 'payroll_lab/calc_inss.html', context=my_context)


class CalcIrrfView(View, SideBarMixin):

    def get(self, request):

        my_context = self.get_context_sidebar(SideBarPL.URL_ID_PLAY)

        # Render the HTML template index.html with the data in the context variable
        return render(request, 'payroll_lab/gitcalc_irrf.html', context=my_context)