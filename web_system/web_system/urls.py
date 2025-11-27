"""
URL configuration for web_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import  index, contact
from .views.contact_view import ContactView
from django.contrib.auth import views as auth_views
from web_system.forms.custom_login_form import CustomLoginForm
from .views.profile import ProfileView

urlpatterns = [
    path('',index, name='index'),
    path('admin/', admin.site.urls),
    path('relacionamentos/', include('relacionamentos.urls')),
    path('funcao/contato', contact, name='contact_function'),
    path('classe/contato', ContactView.as_view(), name='class_contact'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=CustomLoginForm)),
    path('accounts/',include('django.contrib.auth.urls')),
    #path('funcao/search/', views.buscar, name='search_function')
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('services/', include('services.urls'))

]
