from datetime import date

class Menu():

    def __init__(self, name='', url_id='', active=False, icon=''):
         
         self._name       = name
         self._url_id     = url_id
         self._active     = active
         self._icon       = icon
         self._menu_itens = []

    def __getitem__(self, item): #representa o comportamento de uma lista
        return self._menu_itens[item]

    def __len__(self): #Para poder usar a função len
        return len(self._menu_itens)
    
    @property
    def name(self):
        return self._name
    
    @property
    def url_id(self):
        return self._url_id
    
    @property
    def active(self):
        return self._active
        
    @property
    def icon(self):
        return self._icon
    
    @icon.setter
    def icon(self,icon):
        self._icon   = icon

    @property
    def menu_itens(self):
        return self._menu_itens
    
    @menu_itens.setter
    def menu_itens(self, menu_itens):
        self._menu_itens = menu_itens

    @property
    def active_attrib_for_navbar(self):
        if (self._active == True):
            return ' active '
        else:
            return ''
    @property
    def active_attrib1_for_sidebar(self):
        if (self._active == True):
            return ' collapsed '
        else:
            return ' collapse '

    @property
    def active_attrib2_for_sidebar(self):
        if (self._active == True):
            return 'collapse show'
        else:
            return 'collapse'
        
    @property
    def active_expand_for_sidebar(self):
        if (self._active == True):
            return 'true'
        else:
            return 'false'
        
    def __str__(self):
        return f'Name: {self._name} - URL id: {self._url_id} - Active: {self._active} - Itens: {self.menu_itens}'


class NavBar(Menu):

    URL_ID_HOME    = 'index'
    URL_ID_PL      = 'payroll_lab'
    URL_ID_PROFILE = 'profile'
            
    def __init__(self, active_item_name):

        super().__init__()

        menu_active = active_item_name == NavBar.URL_ID_HOME
        menu_home    = Menu('Home', NavBar.URL_ID_HOME, menu_active, 'fas fa-home')

        menu_active = active_item_name == NavBar.URL_ID_PL
        menu_pl      = Menu('Payroll Lab', NavBar.URL_ID_PL, menu_active, 'fas fa-compass-drafting')

        menu_active = active_item_name == NavBar.URL_ID_PROFILE
        menu_profile = Menu('Sobre o Autor', NavBar.URL_ID_PROFILE, menu_active, 'fas fa-user-ninja')

        self._menu_itens = [menu_home, menu_pl, menu_profile]


class SideBarPL(Menu):

    URL_ID_CONF      = 'conf'
    URL_ID_PLAY      = 'play'
    URL_ID_INSS      = 'inss'
    URL_ID_IRRF      = 'irrf'
    URL_ID_CAD_EE    = 'cad_ee'
    URL_ID_CALC_INSS = 'calc_inss'
    URL_ID_CALC_IRRF = 'calc_irrf'

    def __init__(self, active_item_name=''):
        super().__init__()

        menu_active = (active_item_name == SideBarPL.URL_ID_CONF)

        submenu_conf = Menu('Configuração', SideBarPL.URL_ID_CONF, menu_active, 'fa-list-check')
        menu_item_tab_inss = Menu('Tabela de INSS', SideBarPL.URL_ID_INSS, icon='fa-table-list')    
        menu_item_tab_irrf = Menu('Tabela de IRRF', SideBarPL.URL_ID_IRRF, icon='fa-table-list')
        submenu_conf.menu_itens = [menu_item_tab_inss, menu_item_tab_irrf,]

        menu_active = (active_item_name == SideBarPL.URL_ID_PLAY)   

        submenu_play = Menu('Playground', SideBarPL.URL_ID_PLAY, menu_active, 'fa-laptop-code')
        menu_item_cad_ee = Menu('Cadastro de Empregado', SideBarPL.URL_ID_CAD_EE, icon='fa-address-card')
        menu_item_calc_inss = Menu('Calculo de INSS', SideBarPL.URL_ID_CALC_INSS, icon='fa-sack-dollar')
        menu_item_calc_irrf = Menu('Calculo de IRRF', SideBarPL.URL_ID_CALC_IRRF, icon='fa-sack-dollar')
        submenu_play.menu_itens = [menu_item_cad_ee, menu_item_calc_inss, menu_item_calc_irrf]    

        self.menu_itens = [submenu_conf, submenu_play]

class NavBarMixin(object):

    def get_navbar(self, active_item_name):

        return NavBar(active_item_name)
    
    def get_current_year(self):

        data_atual = date.today()
        return u'%s' % data_atual.year #retorna o ano como string
    
    def get_context_navbar(self, active_item_name):

        navbar = self.get_navbar(active_item_name)
        current_year = self.get_current_year()

        return {
            'navbar':navbar,
            'current_year' : current_year,
        }        
        
    
class SideBarMixin(NavBarMixin):

    def get_sidebar(self, active_item_name):

        return SideBarPL(active_item_name)
    
    def get_context_sidebar(self, active_item_name=''):

        navbar = self.get_navbar(NavBar.URL_ID_PL)
        sidebar = SideBarPL(active_item_name)
        current_year = self.get_current_year()

        return {
            'navbar':navbar,
            'sidebar':sidebar,
            'current_year' : current_year,
        }


if (__name__ == "__main__"):

    navbar = NavBar(NavBar.URL_ID_HOME)

    for menuitem in navbar:
        print(menuitem)

    sidebar = SideBarPL(SideBarPL.URL_ID_PLAY)
    for submenu in sidebar:
        print(submenu)
        if len(submenu.menu_itens) > 0:
            for menuitem in submenu.menu_itens:
                print(f'---- {menuitem}')


