# coding=utf-8
"""
Django settings for ttsx project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 安全cookie盐值 不过好像没启用
SECRET_KEY = 'j=bhwx@axf1yp4j$0#=ux7o2(x$yo)+v#r_8*^43ljj=2k4%l&'

# SECURITY WARNING: don't run with debug turned on in production!

# 调试模式/非调试模式
DEBUG = False

# 允许访问的ip
ALLOWED_HOSTS = ["*"]

# Application definition
# 注册应用
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "haystack",
    "tt_user",
    "tt_goods",
    "tinymce",
    "tt_cart",
    "tt_order",
    "captcha",
)
# 中间件类
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# 根级url处理文件
ROOT_URLCONF = 'ttsx.urls'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 模板目录
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        # 是否应该在每个已安装的应用中查找模板
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# wsgi配置
WSGI_APPLICATION = 'ttsx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# mysql数据库配置
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        "NAME":"ttsx",
        "USER":"root",
        "PASSWORD":"******",
        "HOST":"localhost",
        "PORT":"3306",

    }
}

# redis缓存配置
CACHES = {
    "default":{
        # 设定缓存到本地redis
        "BACKEND":"redis_cache.cache.RedisCache",
        # 缓存主机
        "LOCATION":"localhost:6379",
        # 缓存有效期
        "TIMEOUT":3600,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# 语言配置
LANGUAGE_CODE = 'zh-Hans'#'en-us'
# 地区时间配置
TIME_ZONE = "Asia/Shanghai"#'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False #True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# 配置静态文件url
STATIC_URL = '/static/'

# 配置静态文件的路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static")
]

# 配置session使用redis
SESSION_ENGINE = "redis_sessions.session"
SESSION_REDIS_HOST = "localhost"
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = ""
SESSION_REDIS_PREFIX = "session"

# 配置测试状态下文件上传路径
MEDIA_ROOT = os.path.join(BASE_DIR,"static")
# 配置部署状态下文件上传路径
# MEDIA_ROOT = "/var/www/ttsx/static/"

# 配置富文本编辑器在admin的显示
TINYMCE_DEFAULT_CONFIG = {
    "theme":"advanced",
    "width":800,
    "height":400,
}

# 添加搜索引擎
HAYSTACK_CONNECTIONS = {
    'default': {
        # 指定使用的搜索引擎
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 指定索引文件存放位置
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

#新增的数据自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# 分页输出值
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

# 验证码前景色
CAPTCHA_FOREGROUND_COLOR = '#47aa34'
# 验证码有效期
CAPTCHA_TIMEOUT = 2