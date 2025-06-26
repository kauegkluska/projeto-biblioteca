"""
Django settings for biblioteca project.

Configurações do projeto Django 'biblioteca' geradas automaticamente pela ferramenta django-admin.

Referências para documentação oficial:
- Guia geral de settings: https://docs.djangoproject.com/en/5.2/topics/settings/
- Lista completa de configurações: https://docs.djangoproject.com/en/5.2/ref/settings/
"""
from decouple import config
from pathlib import Path
import os

#: Caminho base do projeto.
#: @type Path
BASE_DIR = Path(__file__).resolve().parent.parent

#: Chave secreta usada para segurança e criptografia do Django.
#: IMPORTANTE: mantenha esta chave protegida em produção.
#: @type str
SECRET_KEY = config('SECRET_KEY')

#: Ativa/desativa o modo debug. Deve ser False em produção.
#: @type bool
DEBUG = True

#: Lista de domínios permitidos a fazer requisições.
#: Exemplo: ['localhost', 'meusite.com']
#: @type list[str]
ALLOWED_HOSTS = []

#: Lista de apps instalados no projeto.
#: Inclui apps do Django e aplicativos personalizados.
#: @type list[str]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

#: Lista de middlewares aplicados em cada requisição/resposta.
#: São responsáveis por segurança, sessões, autenticação, etc.
#: @type list[str]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#: Caminho para o arquivo de configuração de rotas do projeto.
#: @type str
ROOT_URLCONF = 'biblioteca.urls'

#: Configurações do sistema de templates Django.
#: Define mecanismo de renderização e processadores de contexto.
#: @type list[dict]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#: Ponto de entrada WSGI da aplicação Django.
#: @type str
WSGI_APPLICATION = 'biblioteca.wsgi.application'

#: Configuração do banco de dados.
#: Utiliza SQLite como backend para desenvolvimento.
#: @type dict
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#: Lista de validadores de senha aplicados ao cadastro/autenticação de usuários.
#: @type list[dict]
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#: Código de idioma padrão do projeto (en-us, pt-br, etc.)
#: @type str
LANGUAGE_CODE = 'pt-br'

LANGUAGES=[
    ('pt-br','Português'),
    ('en', 'English'),
    ('es', 'Español'),
]
# Onde os arquivos de tradução ficarão armazenados
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

#: Fuso horário padrão da aplicação.
#: @type str
TIME_ZONE = 'UTC'

#: Ativa o sistema de internacionalização (i18n).
#: @type bool
USE_I18N = True

#: Ativa suporte ao uso de timezones (fuso horário).
#: @type bool
USE_TZ = True

#: URL base para servir arquivos estáticos.
#: Exemplo: '/static/'
#: @type str
STATIC_URL = 'static/'

#: Tipo padrão de campo para chaves primárias nas models.
#: @type str
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
