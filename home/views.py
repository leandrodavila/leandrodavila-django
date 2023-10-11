from django.shortcuts import render
from django.views import View
from home.navigation import NavBar, NavBarMixin

from django.conf import settings
from django.shortcuts import redirect

class IndexView(View, NavBarMixin):

    def get(self, request):

        navbar = self.get_navbar(NavBar.URL_ID_HOME)
        current_year = self.get_current_year()

        sidebar = {
            'navbar':navbar,
            'current_year' : current_year,
        }

        my_context = self.get_context_navbar(NavBar.URL_ID_HOME)

        # Render the HTML template index.html with the data in the context variable
        return render(request, 'home/index.html', context=my_context)

class ProfileView(View, NavBarMixin):

    def get(self, request):

        navbar = self.get_navbar(NavBar.URL_ID_PROFILE)
        current_year = self.get_current_year()
        
        sidebar = {
            'navbar':navbar,
            'current_year' : current_year,
        }

        # Render the HTML template index.html with the data in the context variable
        return render(request, 'home/profile.html', context=sidebar)

class IconsView(View, NavBarMixin):

    def get(self, request):

        navbar = self.get_navbar(NavBar.URL_ID_HOME)
        current_year = self.get_current_year()

        sidebar = {
            'navbar':navbar,
            'current_year' : current_year,
        }
        
        # Render the HTML template index.html with the data in the context variable
        return render(request, 'home/icons.html', context=sidebar)

def error_404_view(request, exception):
   
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')
