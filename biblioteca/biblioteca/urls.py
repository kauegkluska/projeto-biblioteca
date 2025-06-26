"""
URL configuration for biblioteca project.

This module defines the URL routing for the Django project.

For more information, see:
https://docs.djangoproject.com/en/5.2/topics/http/urls/

Examples
--------
Function views:
    1. Import a view: from my_app import views
    2. Add a route: path('', views.home, name='home')

Class-based views:
    1. Import a class-based view: from other_app.views import Home
    2. Add a route: path('', Home.as_view(), name='home')

Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a route: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
"""
: Lista de padrões de URL do projeto.
:
: - `'admin/'`: URL para o painel administrativo do Django.
: - `''` (vazio): inclui as URLs definidas na aplicação `core`.
:
: @type list[django.urls.path]
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
