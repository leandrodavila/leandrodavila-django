from django.urls import path
from home import views as home_views
from home.views import IndexView, ProfileView, IconsView
from django.conf.urls import handler404, handler500


urlpatterns = [
    #path('', home_views.index, name='index'),
    #path('index/', home_views.index, name='index'),
    #path('profile/', home_views.profile, name='profile'),

    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('icons/',IconsView.as_view(), name='icons'),
]
